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
    domain = Field(str, max_length=10, verbose_name='领域',
                   choices=functions.parameter_choices('domain'))
    source = Field(str, max_length=10, verbose_name='来源',
                   choices=functions.parameter_choices('source'))
    deploy = Field(str, max_length=10, verbose_name='部署',
                   choices=functions.parameter_choices('deploy'))
    responsible = Reference('user', verbose_name='责任人', index=True)
    plan_begin_date = Field(DATE, verbose_name='开始时间')
    plan_finish_date = Field(DATE, verbose_name='结束时间')
    version_date = Field(DATE, verbose_name='上线时间', index=True)
    percent = Field(int, verbose_name='完成%')
    priority = Field(str, max_length=10,
                         choices=functions.parameter_choices('issue_priority'),
                         verbose_name='优先级')
    status = Field(str, max_length=10,
                       choices=functions.parameter_choices('issue_status'),
                       verbose_name='状态')
    page_num = Field(int, verbose_name='页面数')
    trans_num = Field(int, verbose_name='交易数')

    class Table:
        fields = [
            {'name':'content.id', 'title':'ID', 'width':40, 'align':'center'},
            {'name':'contentdetailissue.domain', 'align':'center', 'width':80},
            {'name':'content.category', 'align':'center', 'width':80},
            # {'name':'content.group', 'hidden':True},
            #{'name':'content.content_type'},
            {'name':'content.title', 'width':300},
            {'name':'contentdetailissue.priority', 'align':'center', 'width':60},
            {'name':'contentdetailissue.source', 'align':'center', 'width':80},
            {'name':'contentdetailissue.responsible', 'align':'center', 'width':80},
            {'name':'contentdetailissue.deploy', 'align':'center', 'width':80},
            {'name':'contentdetailissue.page_num', 'align':'center', 'width':60},
            {'name':'contentdetailissue.trans_num', 'align':'center', 'width':60},
            {'name':'contentdetailissue.plan_begin_date', 'align':'center', 'width':100},
            {'name':'contentdetailissue.plan_finish_date', 'align':'center', 'width':100},
            {'name':'contentdetailissue.status', 'align':'center', 'width':60},
            {'name':'contentdetailissue.percent', 'align':'center', 'width':80},
            # {'name':'content.memo', 'width':80},
            {'name':'content.labels', 'hidden':True},
            {'name':'content.creator', 'align':'center', 'width':80, 'hidden':True},
            {'name':'content.hits', 'hidden':True},
            {'name':'content.created_time', 'hidden':True},
            #{'name':'content.modified_time'},
            {'name':'contentdetailissue.version_date', 'align':'center', 'width':100},
        ]

    class Batch:
        fields = [
            {'name':'content.id', 'title':'ID'},
            #{'name':'content.group', 'hidden':True},
            #{'name':'content.content_type'},
            {'name':'contentdetailissue.domain', 'editor':'select', 'selectOptions':get_source('domain')},
            {'name':'content.category', 'editor':'select', 'selectOptions':get_source('issue_category')},
            {'name':'content.title'},
            {'name':'contentdetailissue.priority', 'editor':'select', 'selectOptions':get_source('issue_priority')},
            {'name':'contentdetailissue.source', 'editor':'select', 'selectOptions':get_source('source')},
            {'name':'contentdetailissue.responsible'},
            {'name':'contentdetailissue.deploy', 'editor':'select',
                'selectOptions':get_source('deploy')},
            {'name':'contentdetailissue.page_num'},
            {'name':'contentdetailissue.trans_num'},
            {'name':'contentdetailissue.plan_begin_date'},
            {'name':'contentdetailissue.plan_finish_date'},
            {'name':'contentdetailissue.status', 'editor':'select', 'selectOptions':get_source('issue_status')},
            {'name':'contentdetailissue.percent'},
            {'name':'contentextend.memo', 'width':80},
            {'name':'content.labels', 'hidden':True},
            {'name':'content.creator'},
            {'name':'content.hits', 'hidden':True},
            {'name':'content.created_time', 'hidden':True},
            #{'name':'content.modified_time'},
            {'name':'contentdetailissue.version_date'},
            {'name':'contentextend.content'},
        ]

    class AddForm:
        fields = [
            'category',
            'domain',
            'source',
            'title', 'priority',
            'version_date',
            'plan_begin_date', 'plan_finish_date',
            'percent',
            'responsible',
            'page_num',
            'trans_num',
            'content',
            'memo',
            'uuid',
        ]

        layout = [
            'title',
            'content',
            'memo',
            ['plan_begin_date', 'plan_finish_date', 'percent'],
            'version_date',
            'responsible',
            ['page_num', 'trans_num'],
            'category',
            'domain',
            'source',
            'priority',
        ]

    class EditForm:
        fields = [
            'category',
            'domain',
            'source',
            'title', 'priority',
            'version_date',
            'plan_begin_date', 'plan_finish_date',
            'percent',
            'responsible',
            'page_num',
            'trans_num',
            'content',
            'memo',
            'status',
        ]

        layout = [
            'title',
            'content',
            'memo',
            ['status', 'percent'],
            ['plan_begin_date', 'plan_finish_date'],
            'version_date',
            'responsible',
            ['page_num', 'trans_num'],
            'category',
            'domain',
            'source',
            'priority',
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
    def get_domain_data(cls, domain, condition=None):
        from sqlalchemy import and_

        C = functions.get_model('content')

        cond = and_(cls.c.content_id==C.c.id,
                         cls.c.domain==domain, condition)

        return cls.filter(cond)