#coding=utf-8

from uliweb.orm import *
from content.models import ContentDetail

class ContentDetailTicket(ContentDetail):
    """
    需求、问题类型
    """
    responsible = Reference('user', verbose_name='责任人', index=True)
    plan_begin_date = Field(DATE, verbose_name='开始时间')
    plan_finish_date = Field(DATE, verbose_name='结束时间')
    version_date = Field(DATE, verbose_name='上线时间', index=True)
    percent = Field(int, verbose_name='完成百分比')
    priority = Reference('parametervalues', reference_fieldname='value', verbose_name='优先级')
