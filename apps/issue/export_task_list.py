#coding=utf8
# 导出开发测试任务跟踪表

from uliweb import functions
from uliweb.utils import date
from uliweb.orm import do_
from openpyxl import Workbook
from sqlalchemy import select, and_

def call(args, options, global_options):
    process()

def process():
    C = functions.get_model('content')
    D = functions.get_model('contentdetailissue')
    E = functions.get_model('contentextend')
    User = functions.get_model('user')
    today = date.today()

    filename = 'task_list_{}.xlsx'.format(today.strftime('%Y%m%d'))
    wb = Workbook()
    ws = wb.create_sheet()

    query = select([C.c.id, D.c.task_id, C.c.title, E.c.summary, C.c.category, D.c.status,
                    User.c.nickname, D.c.source, C.c.created_time,
                    D.c.submitted_date, D.c.cooperate_system,
                    D.c.cooperate_task, D.c.cooperate_test,
                    D.c.trans_num, D.c.deploy],
                        and_(C.c.id==E.c.content_id,
                            C.c.id==D.c.content_id,
                            D.c.responsible==User.c.id,
                            D.c.milestone==1,
                            D.c.status.in_(['01', '03', '05', '08', '09', '10']),
                            D.c.in_task_list==True,
                            C.c.category.in_(['issue', 'reqbase',
                                              'reqother', 'sysimp', 'sysbug', 'chenting']),
                            C.c.deleted==False,
                             )
                      )

    n = 0
    ws.append([u'1_序号',
               u'2_项目',
               u'3_责任开发小组',
               u'4_模块',
               u'5_任务类型',
               u'6_是否已协调其他组件',
               u'7_开发任务简述',
               u'8_计划投产版本',
               u'9_当前阶段',
               u'10_涉及增加/修改的交易或模块',
               u'11_是否涉及P8及处室人员开发',
               u'12_开发人员安排',
               u'13_任务来源',
               u'14_任务来源说明',
               u'15_任务来源日期',
               u'16_配合开发组件/系统',
               u'17_配合开发事项',
               u'18_配合测试组件/系统',
               u'19_测试环境',
               u'20_测试人员',
               u'21_当前测试问题描述',
               u'ID'
               ])
    for row in do_(query):
        if row.category in ['reqbase']:
            type = u'A-常规需求'
        elif row.category in ['reqother']:
            type = u'B-小规模需求'
        # elif row.category in ['issue', 'sysbug', 'chenting']:
        #     _type = u'B-生产优化'
        # else:
        #     _type = u'B-技术改造'
        else:
            type = u'B-生产优化'

        if row.status == '01':
            status = u'提出'
        elif row.status == '03':
            status = u'开发'
        elif row.status in ('05', '08', '09'):
            status = u'测试'
        else:
            status = u'完成'

        if row.source in ('issue', 'bug', 'email', 'chenting'):
            source = u'运维支持'
        elif row.source == 'letter':
            source = u'函件'
        elif row.source == 'prj_meeting':
            source = u'项目例会'
        elif row.source == 'p_meeting':
            source = u'生产例会'
        elif row.source == 'trans_meeting':
            source = u'迁移例会'
        elif row.source == 'reqbase':
            source = u'新需求'
        else:
            source = u'其它'

        if row.deploy == 'ITM' and row.trans_num > 0:
            p8_deploy = u'是'
        else:
            p8_deploy = u'否'

        time = row.submitted_date or row.created_time

        d = [#开发任务整体情况
             row.task_id, 'ITDM', u'开发三组', 'ITDM', type, '',
             row.title, '20170729', status,
             #开发任务详细情况
             row.summary, p8_deploy, row.nickname, source, '',
             #关联组件配合情况
             date.to_date(time), row.cooperate_system, row.cooperate_task,
             row.cooperate_test,
             #测试情况
             '', '', '',
             row.id,
            ]
        ws.append(d)

        n += 1
    wb.save(filename)
    print 'Total export {} records'.format(n)
