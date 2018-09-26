#coding=utf8

from uliweb.orm import *

class Comment(Model):
    __verbose_name__ = '通用评论'
    key = Field(str, max_length=200, index=True)
    num = Field(int, verbose_name=u'评论数量')

class CommentDetail(Model):
    comment = Reference('comment', collection_name='comments')
    author = Reference('user', verbose_name='作者')
    content = Field(TEXT, verbose_name='内容')
    created_time = Field(DATETIME, verbose_name='创建时间', auto_now_add=True)
    modified_time = Field(DATETIME, verbose_name='修改时间', auto_now_add=True, auto_now=True)
    level = Field(int)
    order = Field(int)