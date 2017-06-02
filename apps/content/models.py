#coding=utf-8

from uliweb import functions
from uliweb.orm import *
from uliweb.utils.common import cached_property
from sqlalchemy.sql import and_, or_

class Content(Model):
    """
    文章类型
    """
    uuid = Field(str, max_length=32)
    group = Reference('usergroup', verbose_name='小组')
    content_type = Reference('contenttype', verbose_name='内容类型', index=True)
    category = Field(str, max_length=10, verbose_name='分类',
                     choices=functions.parameter_choices('issue_category'))
    labels = Field(str, max_length=300, verbose_name='标签') #逗号分隔
    title = Field(str, max_length=200, verbose_name='标题', index=True)
    creator = Reference('user', verbose_name='创建人', index=True)
    hits = Field(int, verbose_name='点击次数')
    deleted = Field(bool, verbose_name='删除', server_default='0')
    created_time = Field(DATETIME, verbose_name='创建时间', auto_now_add=True)
    modified_time = Field(DATETIME, verbose_name='修改时间', auto_now_add=True, auto_now=True)
    version = Field(int)

    def get_key(self):
        """
        获得外部连接时的key，可以重定义为uuid或md5
        :return:
        """
        return 'content:{}'.format(self.id)

    def get_detail(self):
        """
        根据content_type取明细数据
        """
        detail_model = self.content_type.model_name

        D = functions.get_model(detail_model)
        obj = D.get(D.c.content_id==self.id)
        return obj

    def get_content(self):
        """
        根据content_type取内容数据
        """
        D = functions.get_model('contentextend')
        obj = D.get(D.c.content_id==self.id)
        return obj

    def add(self, content_id):
        """
        添加关系
        :return: True添加成功， False已经存在
        """
        R = functions.get_model('contentrelation')
        return R.add(self.id, content_id)

    def clear(self, content_id):
        R = functions.get_model('contentrelation')
        return R.clear(self.id, content_id)

    def relations(self, content_type=None):
        R = functions.get_model('contentrelation')
        return R.objects(self.id, content_type=content_type)

class ContentDetail(Model):
    """
    文章
    """
    content_id = Field(int, verbose_name='内容ID', index=True)
    created_time = Field(DATETIME, verbose_name='创建时间', auto_now_add=True)
    modified_time = Field(DATETIME, verbose_name='修改时间', auto_now_add=True, auto_now=True)

class ContentDetailArticle(ContentDetail):
    """
    文章类型
    """
    pass

class ContentExtend(Model):
    """
    存放内容的扩展内容
    """
    content_id = Field(int)
    content = Field(TEXT, verbose_name='内容')
    info = Field(JSON, verbose_name='扩展信息')
    memo = Field(TEXT, verbose_name='备注')
    created_time = Field(DATETIME, verbose_name='创建时间', auto_now_add=True)
    modified_time = Field(DATETIME, verbose_name='修改时间', auto_now_add=True, auto_now=True)

class ContentRelation(Model):
    """
    用于保存两个内容间的关系
    """
    content_a = Field(int)
    content_b = Field(int)

    @classmethod
    def OnInit(cls):
        Index('content_relation_a', cls.c.content_a, cls.c.content_b, unique=True)
        Index('content_relation_b', cls.c.content_b, cls.c.content_a, unique=True)

    @classmethod
    def _get_id(self, obj):
        if isinstance(obj, Model):
            return obj.id
        else:
            return obj

    @classmethod
    def find(cls, a_id, b_id):
        a_id = cls._get_id(a_id)
        b_id = cls._get_id(b_id)

        obj = cls.get(or_(
                and_(cls.c.content_a==a_id, cls.c.content_b==b_id),
                and_(cls.c.content_b==a_id, cls.c.content_a==b_id)))
        return obj

    @classmethod
    def add(cls, a_id, b_id):
        """
        添加关系
        """
        obj = cls.find(a_id, b_id)
        if not obj:
            obj = cls(content_a=a_id, content_id=b_id)
            obj.save()
        return obj

    @classmethod
    def clear(cls, a_id, b_id):
        """
        清除关系
        :return: 成功删除返回True，否则返回False
        """
        obj = cls.find(a_id, b_id)
        if obj:
            obj.delete()
            return True
        else:
            return False

    @classmethod
    def objects(cls, a_id, content_type=None):
        """
        返回a_id所关系的所有content对象
        :param a_id:
        :return:
        """
        C = functions.get_model('content')

        a_id = cls._get_id(a_id)
        cond1 = and_(C.c.id==cls.c.content_b, C.c.content_a==a_id)
        if content_type:
            cond1 = and_(C.c.content_type==content_type, cond1)
        cond2 = and_(C.c.id==cls.c.content_a, C.c.content_b==a_id)
        if content_type:
            cond2 = and_(C.c.content_type==content_type, cond2)
        condition = or_(cond1, cond2)
        return C.filter(condition)
