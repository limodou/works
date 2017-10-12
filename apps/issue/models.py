#coding=utf-8

from uliweb import functions
from uliweb.orm import *
from content.models import ContentDetail

def get_source(name):
    def _f():
        return [x[1] for x in functions.get_parameter(name)]
    return _f

class ContentDetailIssue(ContentDetail):
    """
    需求、问题类型
    """
    domain = Field(str, max_length=20, verbose_name='领域',
                   choices=functions.parameter_choices('domain'))
    source = Field(str, max_length=20, verbose_name='来源',
                   choices=functions.parameter_choices('source'))
    source_desc = Field(str, max_length=256, verbose_name='来源说明')
    deploy = Field(str, max_length=20, verbose_name='部署',
                   choices=functions.parameter_choices('deploy'))
    responsible = Reference('user', verbose_name='责任人', index=True)
    plan_begin_date = Field(DATE, verbose_name='开始时间')
    plan_finish_date = Field(DATE, verbose_name='结束时间')
    version_date = Field(DATE, verbose_name='上线时间', index=True)
    milestone = Reference('milestone', verbose_name='里程碑')
    percent = Field(int, verbose_name='完成%')
    priority = Field(str, max_length=10,
                         choices=functions.parameter_choices('issue_priority'),
                         verbose_name='优先级')
    status = Field(str, max_length=10,
                       choices=functions.parameter_choices('issue_status'),
                       verbose_name='状态')
    workload = Field(DECIMAL, verbose_name='工作量(人天)', scale=1)
    page_num = Field(int, verbose_name='页面数')
    trans_num = Field(int, verbose_name='交易数')
    batch_num = Field(int, verbose_name='批处理数')
    task_num = Field(int, verbose_name='任务数')
    submitter = Field(str, max_length=80, verbose_name='提出人')
    submitted_date = Field(DATE, verbose_name='提出时间')
    in_task_list = Field(bool, verbose_name='是否加入开发任务跟踪表', default=False, server_default='0')
    task_id = Field(int, verbose_name='任务序号')

    cooperate_system = Field(str, max_length=80, verbose_name='配合组件系统')
    cooperate_task = Field(str, max_length=1024, verbose_name='配合开发事项')
    cooperate_test = Field(str, max_length=256, verbose_name='配合测试组件')

    class Table:
        fields = [
            {'name':'content.id', 'title':'ID', 'width':40, 'align':'center'},
            {'name':'contentdetailissue.domain', 'align':'center', 'width':120, 'sortable': True},
            {'name':'content.category', 'align':'center', 'width':80},
            # {'name':'content.group', 'hidden':True},
            #{'name':'content.content_type'},
            {'name':'content.title', 'width':200},
            {'name':'contentextend.summary', 'width':200, 'verbose_name':'解决方案'},
            {'name':'contentdetailissue.source', 'align':'center', 'width':80},
            {'name':'contentdetailissue.responsible', 'align':'center', 'width':80},
            {'name':'contentdetailissue.status', 'align':'center', 'width':80},
            {'name':'contentdetailissue.milestone', 'align':'center', 'width':90},
            {'name':'contentdetailissue.deploy', 'align':'center', 'width':80},
            {'name':'contentdetailissue.priority', 'align':'center', 'width':60},
            {'name':'contentdetailissue.workload', 'align':'center', 'width':60},
            {'name':'contentdetailissue.page_num', 'align':'center', 'width':60},
            {'name':'contentdetailissue.trans_num', 'align':'center', 'width':60},
            {'name':'contentdetailissue.batch_num', 'align':'center', 'width':60},
            {'name':'contentdetailissue.plan_begin_date', 'align':'center', 'width':100},
            {'name':'contentdetailissue.plan_finish_date', 'align':'center', 'width':100},
            {'name':'contentdetailissue.submitter', 'align':'center', 'width':80},
            {'name':'contentdetailissue.submitted_date', 'align':'center', 'width':100, 'sortable':True},
            {'name':'contentdetailissue.percent', 'align':'center', 'width':80},
            # {'name':'content.memo', 'width':80},
            {'name':'content.labels', 'hidden':True},
            {'name':'content.creator', 'align':'center', 'width':80, 'hidden':True},
            {'name':'content.hits', 'hidden':True},
            {'name':'content.created_time', 'hidden':True},
            #{'name':'content.modified_time'},
            {'name':'contentdetailissue.in_task_list', 'align':'center', 'width':90},
            {'name':'contentdetailissue.task_id', 'align':'center', 'width':90},
        ]

    class Download:
        fields = [
            {'name':'content.id', 'title':'ID', 'width':40, 'align':'center'},
            {'name':'contentdetailissue.domain', 'align':'center', 'width':120},
            {'name':'content.category', 'align':'center', 'width':80},
            # {'name':'content.group', 'hidden':True},
            #{'name':'content.content_type'},
            {'name':'content.title', 'width':300},
            {'name':'contentdetailissue.source', 'align':'center', 'width':80},
            {'name':'contentdetailissue.source_desc', 'width':80},
            {'name':'contentdetailissue.responsible', 'align':'center', 'width':80},
            {'name':'contentdetailissue.status', 'align':'center', 'width':80},
            {'name':'contentdetailissue.milestone', 'align':'center', 'width':90},
            {'name':'contentdetailissue.deploy', 'align':'center', 'width':80},
            {'name':'contentdetailissue.priority', 'align':'center', 'width':60},
            {'name':'contentdetailissue.workload', 'align':'center', 'width':60},
            {'name':'contentdetailissue.page_num', 'align':'center', 'width':60},
            {'name':'contentdetailissue.trans_num', 'align':'center', 'width':60},
            {'name':'contentdetailissue.batch_num', 'align':'center', 'width':60},
            {'name':'contentdetailissue.plan_begin_date', 'align':'center', 'width':100},
            {'name':'contentdetailissue.plan_finish_date', 'align':'center', 'width':100},
            {'name':'contentdetailissue.submitter', 'align':'center', 'width':80},
            {'name':'contentdetailissue.submitted_date', 'align':'center', 'width':100, 'sortable':True},
            {'name':'contentdetailissue.percent', 'align':'center', 'width':80},
            # {'name':'content.memo', 'width':80},
            {'name':'content.labels', 'hidden':True},
            {'name':'content.creator', 'align':'center', 'width':80, 'hidden':True},
            {'name':'content.hits', 'hidden':True},
            {'name':'content.created_time', 'hidden':True},
            #{'name':'content.modified_time'},
            {'name':'contentextend.content', 'width':400},
            {'name':'contentextend.memo', 'width':200},
            {'name':'contentextend.summary', 'width':200, 'verbose_name':'解决方案'},
            {'name':'contentdetailissue.in_task_list', 'align': 'center', 'width': 90},
            {'name':'contentdetailissue.task_id', 'align': 'center', 'width': 90},
            {'name':'contentdetailissue.cooperate_system', 'width': 90},
            {'name':'contentdetailissue.cooperate_task', 'width': 90},
            {'name':'contentdetailissue.cooperate_test', 'width': 90},
        ]

    class Batch:
        fields = [
            {'name':'content.id', 'title':'ID'},
            #{'name':'content.group', 'hidden':True},
            #{'name':'content.content_type'},
            {'name':'contentdetailissue.domain', 'editor':'select', 'selectOptions':get_source('domain')},
            {'name':'content.category', 'editor':'select', 'selectOptions':get_source('issue_category')},
            {'name':'content.title'},
            {'name':'contentdetailissue.source', 'editor':'select', 'selectOptions':get_source('source')},
            {'name':'contentdetailissue.source_desc'},
            {'name':'contentdetailissue.responsible'},
            {'name':'contentdetailissue.status', 'editor':'select', 'selectOptions':get_source('issue_status')},
            {'name':'contentdetailissue.milestone', 'editor':'select', 'selectOptions':get_source('milestone')},
            {'name':'contentdetailissue.deploy', 'editor':'select',
                'selectOptions':get_source('deploy')},
            {'name':'contentdetailissue.priority', 'editor':'select', 'selectOptions':get_source('issue_priority')},
            {'name':'contentdetailissue.workload'},
            {'name':'contentdetailissue.page_num'},
            {'name':'contentdetailissue.trans_num'},
            {'name':'contentdetailissue.batch_num'},
            {'name':'contentdetailissue.plan_begin_date'},
            {'name':'contentdetailissue.plan_finish_date'},
            {'name':'contentdetailissue.submitter'},
            {'name':'contentdetailissue.submitted_date'},
            {'name':'contentdetailissue.percent'},
            # {'name':'contentextend.content'},
            {'name':'contentextend.memo'},
            {'name':'contentextend.summary', 'verbose_name':'解决方案'},
            {'name':'contentdetailissue.in_task_list', 'editor':'select', 'selectOptions': [u'是', u'否']},
            {'name':'contentdetailissue.task_id'},
            {'name':'contentdetailissue.cooperate_system'},
            {'name':'contentdetailissue.cooperate_task'},
            {'name':'contentdetailissue.cooperate_test'},
        ]

    class AddForm:
        fields = [
            'category',
            'domain',
            'source',
            'source_desc',
            'title', 'priority',
            'milestone',
            'plan_begin_date', 'plan_finish_date',
            'percent',
            'responsible',
            'page_num',
            'trans_num',
            'batch_num',
            'content',
            'memo',
            'uuid',
            'status',
            'deploy',
            'submitter',
            'submitted_date',
            'in_task_list',
            'task_id',
            'summary',
            'cooperate_system',
            'cooperate_task',
            'cooperate_test',
            'workload',
        ]

        layout = [
            '-- 基本信息 --',
            'title',
            'content',
            ['submitter', 'submitted_date'],
            ['source', 'source_desc'],
            'memo',
            '-- 分类信息 --',
            ['domain', 'category'],
            'priority',
            ['deploy', 'milestone'],
            ['in_task_list', 'task_id'],
            '-- 处理状态 --',
            'responsible',
            'summary',
            ['workload', 'plan_begin_date', 'plan_finish_date'],
            ['status', 'percent'],
            ['page_num', 'trans_num', 'batch_num'],
            '-- 关联组件配合情况 --',
            'cooperate_system',
            'cooperate_task',
            'cooperate_test',
        ]

    class EditForm:
        fields = [
            'category',
            'domain',
            'source',
            'source_desc',
            'title', 'priority',
            'milestone',
            'plan_begin_date', 'plan_finish_date',
            'percent',
            'responsible',
            'page_num',
            'trans_num',
            'batch_num',
            'content',
            'memo',
            'status',
            'deploy',
            'submitter',
            'submitted_date',
            'in_task_list',
            'task_id',
            'summary',
            'cooperate_system',
            'cooperate_task',
            'cooperate_test',
            'workload',
        ]

        layout = [
            '-- 基本信息 --',
            'title',
            'content',
            ['submitter', 'submitted_date'],
            ['source', 'source_desc'],
            'memo',
            '-- 分类信息 --',
            ['domain', 'category'],
            'priority',
            ['deploy', 'milestone'],
            ['in_task_list', 'task_id'],
            '-- 处理状态 --',
            'responsible',
            'summary',
            ['workload', 'plan_begin_date', 'plan_finish_date'],
            ['status', 'percent'],
            ['page_num', 'trans_num', 'batch_num'],
            '-- 关联组件配合情况 --',
            'cooperate_system',
            'cooperate_task',
            'cooperate_test',
        ]

    # class DetailView:
    #     fields = [
    #         'category',
    #         'domain',
    #         'source',
    #         'priority',
    #         'plan_begin_date', 'plan_finish_date',
    #         'responsible',
    #         {'name':'content', 'verbose_name':'内容'},
    #         {'name':'memo', 'verbose_name':'备注'},
    #         {'name':'labels', 'verbose_name':'标签'},
    #         'status'
    #     ]
    #
    #     layout = [
    #         '-- '
    #         'status',
    #         'content',
    #         'memo',
    #         ['plan_begin_date', 'plan_finish_date'],
    #         'responsible',
    #         'labels'
    #     ]

    @classmethod
    def get_data(cls, domain=None, user=None, milestone=None, condition=None):
        from sqlalchemy import and_

        C = functions.get_model('content')

        cond = and_(cls.c.content_id==C.c.id, condition)
        if domain:
            cond = (cls.c.domain==domain) & cond
        if user:
            cond = (cls.c.responsible==user) & cond
        if milestone:
            cond = (cls.c.milestone==milestone) & cond

        return cls.filter(cond)