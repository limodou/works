#coding=utf8

from uliweb.orm import *
from content.models import ContentDetail

class ContentDetailArticle(ContentDetail):
    """
    文章类型
    """
    pass

    class Table:
        fields = [
            {'name':'content.id', 'title':'ID', 'width':40, 'align':'center'},
            {'name':'content.category', 'align':'center', 'width':80},
            # {'name':'content.group', 'hidden':True},
            #{'name':'content.content_type'},
            {'name':'content.title', 'width':300},
            {'name':'content.labels', 'hidden':True},
            {'name':'content.creator', 'align':'center', 'width':80, 'hidden':True},
            {'name':'content.hits', 'hidden':True},
            {'name':'content.created_time', 'hidden':True},
            #{'name':'content.modified_time'},
        ]

    class AddForm:
        fields = [
            'category',
            'title',
            'content',
            'uuid',
        ]

        layout = [
            'title',
            'content',
            'category',
        ]

    class EditForm:
        fields = [
            'category',
            'title',
            'content',
        ]

        layout = [
            'title',
            'content',
            'category',
        ]

