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

        return self._add(self.T,
                         hidden_fields=['uuid'],
                         ok_url=get_url,
                         data={'uuid': uuid},
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

