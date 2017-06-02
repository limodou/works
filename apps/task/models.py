#coding=utf8

from uliweb import functions
from uliweb.orm import *

class Task(Model):
    """
    用于记录任务
    """
    key = Field(str, max_length=200, index=True)
    uuid = Field(str, max_length=32)
    title = Field(str, max_length=256, verbose_name='标题')
    content = Field(TEXT, verbose_name='内容')
    creator = Reference('user', verbose_name='提出人', index=True)
    responsible = Reference('user', verbose_name='责任人', index=True)
    plan_begin_date = Field(DATE, verbose_name='开始时间')
    plan_finish_date = Field(DATE, verbose_name='结束时间')
    finish_date = Field(DATETIME, verbose_name='完成时间')
    priority = Field(str, max_length=10,
                         choices=functions.parameter_choices('task_priority'),
                         verbose_name='优先级')
    status = Field(str, max_length=10,
                       choices=functions.parameter_choices('task_status'),
                       verbose_name='状态')

    parent = Reference()
    has_children = Field(bool)
    created_time = Field(DATETIME, verbose_name='创建时间', auto_now_add=True)
    created_user = Reference('user', verbose_name='创建人')
    deleted_time = Field(DATETIME, verbose_name='删除时间')
    deleted_user = Reference('user', verbose_name='删除人')
    modified_time = Field(DATETIME, verbose_name='修改时间', auto_now_add=True, auto_now=True)
    modified_user = Reference('user', verbose_name='修改人')

    @classmethod
    def OnInit(cls):
        Index('task_idx', cls.c.modified_time, cls.c.responsible)

    class Table:
        fields = [
            'title',
            {'name': 'responsible', 'width': 80, 'align': 'center'},
            {'name': 'priority', 'width': 60, 'align': 'center'},
            {'name': 'status', 'width': 60, 'align': 'center'},
            {'name': 'plan_begin_date', 'width':120, 'align': 'center'},
            {'name': 'plan_finish_date', 'width':120, 'align': 'center'},
            {'name': 'finish_date', 'width':120, 'align': 'center'},
        ]

    class AddForm:
        fields = [
            'title',
            'content',
            'responsible',
            'plan_begin_date',
            'plan_finish_date',
            'priority',
            'uuid',
        ]
        layout = [
            'title',
            'content',
            'responsible',
            ['plan_begin_date', 'plan_finish_date'],
            'priority',
            # 'uuid',
        ]

    class EditForm:
        fields = [
            'title',
            'content',
            'responsible',
            'plan_begin_date',
            'plan_finish_date',
            'priority',
            'status',
            'uuid',
        ]
        layout = [
            'title',
            'content',
            'responsible',
            ['plan_begin_date', 'plan_finish_date'],
            'priority',
            'status',
        ]

    class DetailView:
        fields = [
            'title',
            'content',
            'responsible',
            'plan_begin_date',
            'plan_finish_date',
            'priority',
            'status',
            'uuid',
        ]

        layout = [
            'title',
            'content',
            'responsible',
            ['plan_begin_date', 'plan_finish_date'],
            'priority',
            'status',
        ]


class TaskResult(Model):
    """
    产出物表
    """
    task = Reference('task', index=True, collection_name='results')
    type = Field(str, max_length=10,
                 choices=functions.parameter_choices('task_priority'),
                 verbose_name='类型')
    num = Field(int, verbose_name='数量')
    description = Field(TEXT, verbose_name='说明')
