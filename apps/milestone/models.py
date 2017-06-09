#coding=utf8

from uliweb.orm import *

class Milestone(Model):
    name = Field(str, max_length=80, verbose_name='名称', index=True)
    version_date = Field(DATE, verbose_name='上线时间')
    desc = Field(str, max_length=256, verbose_name='描述')
    muted = Field(bool, verbose_name='是否隐藏')
    deleted = Field(bool)

    def __unicode__(self):
        return self.name

    @classmethod
    def get_milestone(cls, exclude_muted=True):
        condition = cls.c.deleted==False
        if exclude_muted:
            condition = (cls.c.muted==False) & condition
        return [(x.id, x.name) for x in cls.filter(condition).order_by(cls.c.version_date)]

    class Table:
        fields = [
            {'name':'id', 'hidden':True},
            {'name':'name', 'align':'center'},
            {'name':'version_date', 'align':'center'},
            {'name':'desc', 'align':'center'}
        ]

