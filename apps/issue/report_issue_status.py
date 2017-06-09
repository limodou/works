#coding=utf8
# 计算需求/问题的状态统计

from uliweb import functions

def call(args, options, global_options):
    from uliweb.utils.sorteddict import SortedDict

    D = functions.get_model('contentdetailissue')

    status = functions.get_parameter('issue_status')
    domain = functions.get_parameter('domain')

    m = {}
    for d in domain:
        for s in status:
            m[(d[0], s[0])] = 0

    condition = D.c.status.in_(['01', '03', '05'])
    for row in D.filter(None):
        key = row.domain, row.status
        if not row.status:
            print 'No status found for id={}'.format(row.id)
            continue
        m[key] += 1

    print '#',
    for s in status:
        print s[1],
    print
    for d in domain:
        print d[1],
        for s in status:
            print m[(d[0], s[0])],
        print

