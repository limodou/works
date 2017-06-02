#coding=utf-8

from uliweb import functions
from uliweb.orm import *
from uliweb.utils.common import cached_property
from sqlalchemy.sql import and_, or_

class ContentType(Model):
    """
    用于记录文档类型，不同的类型可以有自已的字段，但也有一些是通用字段
    """
    name = Field(str, max_length=80, verbose_name='名称', unique=True, index=True)
    display = Field(str, max_length=100, verbose_name='显示名称')
    model_name = Field(str, max_length=100, verbose_name='Model名')
    created_time = Field(DATETIME, verbose_name='创建时间', auto_now_add=True)
    modified_time = Field(DATETIME, verbose_name='修改时间', auto_now_add=True, auto_now=True)

class ContentTypeExtendColumns(Model):
    """
    用于记录每类文档的扩展字段信息
    """
    content_type = Reference('contenttype')
    name = Field(str, max_length=80, verbose_name='字段名称')
    type = Field(str, max_length=10, verbose_name='字段类型')
    length = Field(int, verbose_name='字段长度')
    presice = Field(int, verbose_name='小数精度')
    required = Field(bool, verbose_name='是否必输')
    created_time = Field(DATETIME, verbose_name='创建时间', auto_now_add=True)
    modified_time = Field(DATETIME, verbose_name='修改时间', auto_now_add=True, auto_now=True)

class ContentTypeLayout(Model):
    """
    用于记录每类文档的字段布局
    """
    content_type = Reference('contenttype')
    name = Field(str, max_length=10, verbose_name='布局名称')
    layout = Field(TEXT, verbose_name='布局信息')
    created_time = Field(DATETIME, verbose_name='创建时间', auto_now_add=True)
    modified_time = Field(DATETIME, verbose_name='修改时间', auto_now_add=True, auto_now=True)
