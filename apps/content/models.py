#coding=utf-8

from uliweb.orm import *

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

class Content(Model):
    """
    文章类型
    """
    group = Reference('usergroup', verbose_name='小组')
    content_type = Reference('contenttype', verbose_name='类型')
    category = Reference('parametervalues', reference_fieldname='value', verbose_name='分类')
    labels = Field(str, max_length=300, verbose_name='标签') #逗号分隔
    title = Field(str, max_length=200, verbose_name='标题')
    creator = Reference('user', verbose_name='创建人')
    hits = Field(int, verbose_name='点击次数')
    created_time = Field(DATETIME, verbose_name='创建时间', auto_now_add=True)
    modified_time = Field(DATETIME, verbose_name='修改时间', auto_now_add=True, auto_now=True)

class ContentDetail(Model):
    """
    文章
    """
    content_id = Field(int, verbose_name='内容ID', index=True)
    created_time = Field(DATETIME, verbose_name='创建时间', auto_now_add=True)
    modified_time = Field(DATETIME, verbose_name='修改时间', auto_now_add=True, auto_now=True)

class ContentDetailArtical(ContentDetail):
    """
    文章类型
    """
    pass

class ContentExtend(Model):
    """
    存放内容的扩展内容
    """
    content_type = Reference('contenttype')
    content_id = Field(int)
    content = Field(TEXT, verbose_name='内容')
    info = Field(JSON, verbose_name='扩展信息')
    created_time = Field(DATETIME, verbose_name='创建时间', auto_now_add=True)
    modified_time = Field(DATETIME, verbose_name='修改时间', auto_now_add=True, auto_now=True)
