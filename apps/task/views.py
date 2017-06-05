#coding=utf-8
from uliweb import expose, functions

def __begin__():
    return functions.require_login()

@expose('/task')
class TaskView(functions.MultiView):
    def __init__(self):
        self.T = functions.get_model('task')

    def _get_query_view(self):
        from uliweb_layout.form.query_view import QueryModelView
        from uliweb.utils.generic import ReferenceSelectField

        QueryForm = functions.get_form('QueryForm')
        User = functions.get_model('user')

        responsible = ReferenceSelectField('user', query=User.all().order_by(User.c.username.asc()))

        fields = [
            {'name': 'title', 'like': '%_%'},
            {'name': 'priority', 'multiple':True},
            {'name': 'status', 'multiple':True},
            {'name': 'responsible', 'choices':responsible.get_choices(), 'type':'select', 'label':'责任人'},
        ]
        layout = [
            ['title', 'responsible', 'status'],
            ['priority'],
        ]
        query = QueryModelView(self.T, fields=fields, layout=layout, form_cls=QueryForm)
        return query

    def _convert_title(self, value, obj):
        return u'<a href="/task/view/{}">{}</a>'.format(obj.id, value)

    def _convert_content(self, value, obj):
        return value

    @expose('')
    def list(self):
        queryview = self._get_query_view()
        return self._list(self.T,
                          queryview=queryview,
                          queryform=queryview.get_json(),
                          fields_convert_map=['title'])

    def get(self):
        key = request.GET.get('index')
        query = self.T.filter(self.T.c.key==key).order_by(self.T.c.modified_time.desc())
        if not query.count():
            return json({'success': True, 'count': 0, 'tasks': []})
        else:
            tasks = self._get_tasks(query)
            return json({'success': True, 'count': len(tasks), 'tasks':tasks})

    def _get_task(self, row):
        d = row.to_dict()
        d['creator'] = unicode(row.creator)
        d['responsible'] = unicode(row.responsible) if row.responsible else ''
        d['plan_begin_date'] = row.modified_time.strftime('%Y-%m-%d')
        d['plan_finish_date'] = row.modified_time.strftime('%Y-%m-%d')
        d['finish_date'] = row.modified_time.strftime('%Y-%m-%d %H:%M:%S')
        d['created_time'] = row.modified_time.strftime('%Y-%m-%d %H:%M:%S')
        d['modified_time'] = row.modified_time.strftime('%Y-%m-%d %H:%M:%S')
        # d['group'] = row.modified_time.strftime('%Y-%m-%d') #前端分组用
        return d

    def _get_tasks(self, query):
        s = []
        for row in query.order_by(self.T.c.modified_time.desc()):
            d = self._get_task(row)
            s.append(d)

        return s

    def add(self):
        """
        保存任务

        需要在Query_string传参数：
            parent 表示回复的是哪条信息，目前没有用上
            index 表示对应的键值
        :return:
        """
        from uliweb.utils.common import get_uuid

        key = request.GET.get('index')
        def pre_save(data):
            data['key'] = key
            data['status'] = 'ready'

        def success_data(obj, data):
            return self._get_task(obj)

        def get_url(obj):
            return '/task/view/{}'.format(obj.id)

        uuid = get_uuid()
        data = {'uuid': uuid}
        user_id = request.GET.get('user_id')
        if user_id:
            data['responsible'] = user_id
        status = request.GET.get('status')
        data['status'] = status

        return self._add(self.T,
                         hidden_fields=['uuid'],
                         ok_url=get_url,
                         data=data,
                         template_data={'uuid':uuid},
                         success_data=success_data,
                         pre_save=pre_save,
                         layout_class='bs3t')

    def edit(self, id):
        def success_data(obj, data):
            return self._get_task(obj)

        obj = self.T.get(id)

        return self._edit(self.T,
                          obj=obj,
                          hidden_fields=['uuid'],
                          ok_url='/task/view/{}'.format(id),
                          success_data=success_data,
                          layout_class='bs3t')


    def view(self, id):
        obj = self.T.get(id)

        d = obj.to_display(prefix='dis_')
        return d

    def change(self, id):
        from uliweb.utils import date

        status = request.POST.get('status')

        obj = self.T.get(id)
        obj.status = status
        obj.finish_date = date.now()
        obj.modified_date = date.now()
        obj.modified_user = request.user.id
        obj.save()

        return json({'success': True, 'data': self._get_task(obj)})

    def kanban(self):
        User = functions.get_model('user')

        return {'responsibles':User.get_choices()}

    def _get_card_info(self, row):
        User = functions.get_model('user')

        card = {}

        card['id'] = row.id
        card['title'] = row.title
        card['user'] = unicode(row.responsible or u'未指派')
        if row.responsible:
            card['avater'] = row.responsible.get_image_url()
        else:
            card['avater'] = User.get_default_image_url()
        card['url'] = '/task/view/{}'.format(row.id)
        card['status'] = row.status or 'ready'

        return card

    def get_user_data(self):
        """
        获得某个用户的任务信息
        """
        user_id = request.GET.get('user_id')
        result = []
        status = {}
        for s in functions.get_parameter('task_status'):
            status[s[0]] = x = {'name': s[0], 'title': s[1], 'items': []}
            result.append(x)
        condition = None
        if user_id:
            condition = (self.T.c.responsible==user_id) & condition
        for row in self.T.filter(condition).order_by(self.T.c.modified_time.desc()):
            d = self._get_card_info(row)
            items = status[d['status']]['items']
            items.append(d)

        return json({'success':True, 'data':result})

    def change_status(self, issue_id):
        status = request.GET.get('status')

        obj = self.T.get(issue_id)
        obj.status = status
        obj.save()

        return json({'success':True})