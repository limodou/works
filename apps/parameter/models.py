#coding=utf-8

from uliweb.orm import *

class Parameter(Model):
    """
    文档类型的参数
    """
    content_type = Reference('contenttype')
    name = Field(str, max_length=80, verbose_name='名称', index=True, unique=True)
    display = Field(str, max_length=80, verbose_name='显示名称')
    has_color = Field(bool, verbose_name='是否有颜色')
    created_time = Field(DATETIME, verbose_name='创建时间', auto_now_add=True)
    modified_time = Field(DATETIME, verbose_name='修改时间', auto_now_add=True, auto_now=True)

    class Table:
        fields = [
            'id', 'name', 'display', 'has_color'
        ]

    class AddForm:
        fields = [
            'name', 'display', 'has_color'
        ]

class ParameterValues(Model):
    """
    参数值
    """
    parameter = Reference('parameter')
    value = Field(str, max_length=20, verbose_name='值')
    color = Field(str, max_length=10, verbose_name='颜色值(RGB)')
    order = Field(int, verbose_name='序号')
    display = Field(str, max_length=80, verbose_name='显示名称')
    deleted = Field(bool, verbose_name='是否删除')
    created_time = Field(DATETIME, verbose_name='创建时间', auto_now_add=True)
    modified_time = Field(DATETIME, verbose_name='修改时间', auto_now_add=True, auto_now=True)

    class AddForm:
        fields = [
            'value', 'display', 'order'
        ]

    EditForm = AddForm

    class Table:
        fields = [
            {'name': 'value', 'align': 'center'},
            {'name': 'display', 'align': 'center'},
            {'name': 'order', 'align': 'center'},
        ]