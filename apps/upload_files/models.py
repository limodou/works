#coding=utf8

from uliweb import functions
from uliweb.orm import *
from uliweb.utils import date

class UploadFiles(Model):
    """
    保存上传文件
    """
    key = Field(str, max_length=200, verbose_name='键值', index=True) #用于区分不同的关联记录
    filename = Field(str, max_length=200, verbose_name='文件名')
    filename_path = Field(str, max_length=1024, verbose_name='路径')
    memo = Field(str, max_length=1024, verbose_name='说明')
    enabled = Field(bool, verbose_name='是否有效') #用户未提交时，状态是无效状态
    deleted = Field(bool, verbose_name='是否删除')
    created_time = Field(DATETIME, verbose_name='创建时间', auto_now_add=True)
    created_user = Reference('user', verbose_name='创建人')
    deleted_time = Field(DATETIME, verbose_name='删除时间')
    deleted_user = Reference('user', verbose_name='删除人')
    modified_time = Field(DATETIME, verbose_name='修改时间', auto_now_add=True, auto_now=True)
    modified_user = Reference('user', verbose_name='修改人')

    @classmethod
    def save_request_file(cls, key, path, memo='', file_fieldname='upload'):
        """
        根据request来保存文件
        :param file_fieldname:
        :return:
        """
        import os
        from uliweb import request

        filename = request.files[file_fieldname].filename
        fname = os.path.join(path, filename)
        filename_path = functions.save_file(fname, request.files[file_fieldname])

        return cls.save_file(key, filename, filename_path, memo=memo)

    @classmethod
    def save_file(cls, key, filename, filename_path, memo=''):
        from uliweb import request

        user = None
        if hasattr(request, 'user') and request.user:
            user = request.user
        obj = cls(key=key, filename=filename, filename_path=filename_path, memo=memo,
                  created_user=user, modified_user=user)
        obj.save()
        return obj

    @classmethod
    def get_files(cls, key, include_deleted=False, order_by=None):
        order_by = order_by or cls.c.created_time.asc()
        condition = (cls.c.key==key) & (cls.c.enabled==True) & (cls.c.deleted==include_deleted)
        return cls.filter(condition).order_by(order_by)

    def delete_file(self):
        user = None
        if hasattr(request, 'user') and request.user:
            user = request.user

        now = date.now()

        self.deleted_time = now
        self.deleted_user = user
        return self.save()

    @classmethod
    def clear_data(cls, days, count=5000):
        """
        数据清除，将指定天数之前未生效的记录删除
        :param days: 天数
        :param count: 每次删除条数，可忽略
        :return:
        """
        from datetime import timedelta
        from sqlalchemy import and_

        now = date.now()

        condition = and_(cls.c.enabled==False, cls.c.created_time<(now-timedelta(days=days)))

        c = cls.filter(condition).count()
        if c:
            delete_sql = cls.table.delete().where(condition)
            do_(delete_sql)
        return c
