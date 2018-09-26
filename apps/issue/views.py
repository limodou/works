#coding=utf-8
from __future__ import print_function, absolute_import, unicode_literals
from uliweb import expose, functions
from uliweb.utils._compat import u, string_types

@expose('/issue')
class IssueView(functions.MultiView):
    content_type = 'issue'

    def __begin__(self):
        return functions.require_login()

    def __init__(self):
        #获取issue 内容类型对象
        self.content_type_obj = functions.get_content_type(self.content_type)

        self.C = functions.get_model('content') #主表
        self.D = functions.get_model(self.content_type_obj.model_name) #明细表
        self.E = functions.get_model('contentextend') #扩展表

        M = functions.get_model('milestone')
        self.milestone = M.get_milestone()


    def _get_query_view(self):
        from uliweb_layout.form.query_view import QueryView
        from uliweb.utils.generic import ReferenceSelectField

        QueryForm = functions.get_form('QueryForm')
        User = functions.get_model('user')
        M = functions.get_model('milestone')

        responsible = ReferenceSelectField('user', query=User.all().order_by(User.c.username.asc()))

        fields = [
            {'name': 'title', 'type':'str', 'label':'标题/ID:'},
            {'name': 'category', 'type':'select', 'multiple': True, 'label':'分类:',
                'choices':functions.get_parameter('issue_category')},
            {'name': 'domain', 'type': 'select', 'multiple': True, 'label': '领域:',
             'choices': functions.get_parameter('domain')},
            {'name': 'source', 'type':'select', 'multiple': True, 'label':'来源:',
                'choices':functions.get_parameter('source')},
            {'name': 'status', 'type':'select', 'multiple': True, 'label':'状态:',
                'choices':functions.get_parameter('issue_status')},
            {'name': 'deploy', 'type':'select', 'label':'部署:',
                'choices':functions.get_parameter('deploy')},
            {'name': 'milestone', 'type':'select', 'label':'里程碑:',
                'choices':self.milestone},
            {'name': 'responsible', 'choices':responsible.get_choices(), 'type':'select', 'label':'责任人'},
            {'name': 'submitter', 'type':'str', 'label':'提出人'},
            {'name': 'submitted_date', 'type':'date', 'range':True, 'label':'提出时间'},
            {'name': 'in_task_list', 'type':'select',
                'choices':[('0', '否'), ('1', '是')],
                'label':'是否在开发任务列表中'},
        ]
        layout = [
            ['title', 'domain', 'status'],
            ['submitter', 'submitted_date'],
            ['responsible', 'source', 'category'],
            ['deploy', 'milestone', 'in_task_list']
        ]
        query = QueryView(fields=fields, layout=layout, form_cls=QueryForm)
        return query

    def _get_list(self, **kwargs):
        C = self.C
        D = self.D
        E = self.E
        condition = (C.c.id==D.c.content_id) & (C.c.id==E.c.content_id) & (C.c.deleted==False)
        if kwargs.get('condition') is not None:
            condition = kwargs.pop('condition') & condition
        kwargs['condition'] = condition
        return self._select_list(model=D, **kwargs)

    @expose('')
    def list(self):
        """
        显示需求/问题清单
        :return:
        """

        query = self._get_query_view()
        c = query.run()
        condition = None

        if c.get('title'):
            condition = (self.C.c.id.like(c['title']) | self.C.c.title.like('%'+c['title']+'%')) & condition
        if c.get('category'):
            condition = (self.C.c.category.in_(c['category'])) & condition
        if c.get('source'):
            condition = (self.D.c.source.in_(c['source'])) & condition
        if c.get('deploy'):
            condition = (self.D.c.deploy==c['deploy']) & condition
        if c.get('domain'):
            condition = (self.D.c.domain.in_(c['domain'])) & condition
        if c.get('status'):
            condition = (self.D.c.status.in_(c['status'])) & condition
        if c.get('responsible'):
            condition = (self.D.c.responsible==c['responsible']) & condition
        if c.get('milestone'):
            condition = (self.D.c.milestone==c['milestone']) & condition
        if c.get('in_task_list'):
            condition = (self.D.c.in_task_list==(c['in_task_list']=='1')) & condition

        def content_title(value, obj):
            return u'<a href="/issue/view/{}" target="_blank">{}</a>'.format(obj['content.id'],
                                                            obj['content.title'])

        def in_task_list(value, obj):
            if value:
                return u'是'
            else:
                return u'否'

        return self._get_list(queryview=query,
                              queryform=query.get_json(),
                              condition=condition,
                              fields_convert_map={'content.title': content_title,
                                                  'contentdetailissue.in_task_list': in_task_list
                                                  })

    def batch(self):
        """
        批量录入界面
        :return:
        """
        from uliweb.utils.generic import get_columns


        def post_run(view, result):
            columns = []
            columns_name = []
            for i, col in enumerate(view.table_info['fields_list']):
                if not col.get('hidden'):
                    columns_name.append(col['title'])
                    d = {'data': i}
                    d.update(col)
                    columns.append(d)
            result['columns'] = columns
            result['columns_name'] = columns_name

        def render_func(data, row):
            return [x[1] for x in data]

        condition = self.D.c.id!=self.D.c.id
        return self._select_list(model=self.D,
                                 condition=condition,
                                 post_run=post_run, meta='Batch',
                                 render=render_func, pagination=False)

    def save(self):
        """保存页面信息"""
        import json as _json
        from uliweb.utils.generic import get_model_columns

        C = self.C
        D = self.D

        columns = []
        for col in get_model_columns(D, meta='Batch'):
            if not col.get('hidden'):
                columns.append(col['name'])

        errors = []
        data = []
        success = 0
        for i, row in enumerate(_json.loads(request.POST['data'])):
            d = zip(columns, row)
            error = self._parse_data(len(errors), d)
            if error == -1:
                continue
            if error:
                data.append(row)
                errors.append(error)
            else:
                success += 1

        if errors:
            return json({'success':False, 'message':'保存成功 {} 记录， 出错 {} 记录'.format(success, len(errors)),
                    'errors':errors, 'data':data})
        else:
            return json({'success':True, 'message':'保存成功 {} 条记录!'.format(success)})

    def add(self):
        """
        增加新记录
        :return:
        """

        from uliweb.utils.common import get_uuid

        def get_form_field(name):
            from uliweb.form import TextField, StringField, SelectField

            Milestone = functions.get_model('milestone')

            if name == 'content':
                return TextField(u'内容')
            if name == 'memo':
                return TextField(u'备注')
            if name == 'summary':
                return TextField(u'解决方案', help_string='简要描述方案，如：可能涉及增加或修改的模块或交易')
            if name == 'title':
                return StringField(u'标题', required=True)
            if name == 'category':
                return SelectField(u'分类', choices=functions.get_parameter('issue_category'))
            if name == 'uuid':
                return StringField()
            if name == 'status':
                return SelectField(u'状态', choices=functions.get_parameter('issue_status'))
            if name == 'deploy':
                return SelectField(u'部署', choices=functions.get_parameter('deploy'))
            if name == 'milestone':
                return SelectField(u'里程碑', choices=self.milestone)

        def pre_save(data):
            content = self.C(content_type=self.content_type_obj.id, title=data['title'],
                             creator=request.user.id,
                             category=data['category'],
                             uuid=data['uuid'])
            content.save()
            data['content_id'] = content.id

        def post_save(obj, data):
            extend = self.E(content_id=obj.content_id,
                            memo=data['memo'],
                            summary=data['summary'],
                            content=data['content'])
            extend.save()

        def get_url(obj):
            return '/issue/view/{}'.format(obj.content_id)

        uuid = get_uuid()
        data = {'uuid':uuid}
        data['status'] = request.GET.get('status', '01')
        data['domain'] = request.GET.get('domain', '')
        data['submitter'] = request.user.nickname

        return self._add('contentdetailissue',
                         pre_save=pre_save,
                         post_save=post_save,
                         hidden_fields=['uuid'],
                         ok_url=get_url,
                         data=data,
                         template_data={'uuid':uuid},
                         get_form_field=get_form_field,
                         layout_class='bs3t')

    def edit(self, id):
        """
        修改记录
        :return:
        """

        content = self.C.get(int(id))
        detail = content.get_detail()
        extend = content.get_content()

        def get_form_field(name, obj):
            from uliweb.form import TextField, StringField, SelectField

            Milestone = functions.get_model('milestone')

            if name == 'content':
                return TextField(u'内容')
            if name == 'memo':
                return TextField(u'备注')
            if name == 'summary':
                return TextField(u'解决方案', help_string='简要描述方案，如：可能涉及增加或修改的模块或交易')
            if name == 'title':
                return StringField(u'标题', required=True)
            if name == 'category':
                return SelectField(u'分类', choices=functions.get_parameter('issue_category'))
            if name == 'status':
                return SelectField(u'状态', choices=functions.get_parameter('issue_status'))
            if name == 'deploy':
                return SelectField(u'部署', choices=functions.get_parameter('deploy'))
            if name == 'milestone':
                return SelectField(u'里程碑', choices=self.milestone)


        def post_save(obj, data):
            from uliweb.utils import date
            from uliweb import request

            content.update(title=data['title'], category=data['category'],
                           modified_user=request.user.id, modified_time=date.now())
            r1 = content.save()

            extend.update(content=data['content'], memo=data['memo'], summary=data['summary'])
            r2 = extend.save()
            return r1 or r2

        data = {'title': content.title,
                'content': extend.content,
                'memo': extend.memo,
                'category': content.category,
                'summary': extend.summary}

        return self._edit(self.D,
                         obj=detail,
                         ok_url='/issue/view/{}'.format(id),
                         post_save=post_save,
                         data=data,
                         get_form_field=get_form_field,
                         layout_class='bs3t',
                         template_data={'uuid':content.uuid},
                    )

    def delete(self, id):
        content = self.C.get(int(id))

        def success_data(data):
            return [{'content.id':int(id)}]

        return self._delete(self.D,
                            obj = content,
                            success_data=success_data,
                            use_delete_fieldname='deleted',
                            json_result=True)

    def _validate_creator(self, value):
        User = functions.get_model('user')
        u = User.filter((User.c.username==value) | (User.c.nickname==value))
        count = u.count()
        if count == 0:
            return False, u'用户{}未找到'.format(value)
        elif count > 1:
            return False, u'用户{}存在多条记录'.format(value)
        else:
            return True, list(u)[0].id

    _validate_responsible = _validate_creator

    def _validate_priority(self, value):
        if not value:
            return True, ''
        values = functions.get_parameter('issue_priority')
        for key, display in values:
            if display == value:
                return True, key
        return False, u'优先级不正确, 应该是 {}'.format(','.join([x[1] for x in values]))

    def _validate_domain(self, value):
        if not value:
            return True, ''
        values = functions.get_parameter('domain')
        for key, display in values:
            if display == value:
                return True, key
        return False, u'领域不正确, 应该是 {}'.format(','.join([x[1] for x in values]))

    def _validate_source(self, value):
        if not value:
            return True, ''
        values = functions.get_parameter('source')
        for key, display in values:
            if display == value:
                return True, key
        return False, u'来源值不正确, 应该是 {}'.format(','.join([x[1] for x in values]))

    def _validate_status(self, value):
        if not value:
            return True, ''
        values = functions.get_parameter('issue_status')
        for key, display in values:
            if display == value:
                return True, key
        return False, u'状态值不正确, 应该是 {}'.format(','.join([x[1] for x in values]))

    def _validate_category(self, value):
        if not value:
            return True, ''
        values = functions.get_parameter('issue_category')
        for key, display in values:
            if display == value:
                return True, key
        return False, u'分类值不正确，应该是 {}'.format(','.join([x[1] for x in values]))

    def _validate_deploy(self, value):
        if not value:
            return True, ''
        values = functions.get_parameter('deploy')
        for key, display in values:
            if display == value:
                return True, key
        return False, u'部署值不正确，应该是 {}'.format(','.join([x[1] for x in values]))

    def _validate_percent(self, value):
        if not value:
            return True, 0
        try:
            if isinstance(value, string_types):
                v = int(value.rstrip('%'))
            else:
                v = int(value)
            return True, v
        except:
            return False, '百分比不正确'

    def _validate_plan_begin_date(self, value):
        from uliweb.utils import date

        if not value:
            return True, 0
        v = date.to_date(value)
        if v:
            return True, v
        else:
            return False, '日期格式不正确，需要为 "yyyy/mm/dd" 或 "yyyy-mm-dd"'

    _validate_plan_finish_date = _validate_plan_begin_date
    _validate_submitted_date = _validate_plan_begin_date

    def _validate_milestone(self, value):
        if not value:
            return True, ''

        for key, display in self.milestone:
            if display == value:
                return True, key
        return False, u'里程碑不正确，应该是 {}'.format(','.join([x[1] for x in values]))

    def _validate_trans_num(self, value):
        if not value:
            return True, 0
        try:
            v = int(value)
            return True, v
        except:
            return False, '数值不正确'

    _validate_page_num = _validate_trans_num

    def _validate_title(self, value):
        if value and len(value)>200:
            return False, '标题不能超过200个字符'
        return True, value

    def _validate_in_task_list(self, value):
        if value == u'是':
            return True, True
        if value == u'否':
            return True, False
        return False, '只能输入"是"或"否"'

    def _parse_data(self, index, data):
        """
        处理一行数据
        :param index: 行号
        :param data: [(column, value), ...]
        :return:
        """
        from uliweb.utils.common import get_uuid

        objs = {}
        errors = []

        for col, (old_column, value) in enumerate(data):
            model_name, column = old_column.split('.')
            d = objs.setdefault(model_name, {})
            validate_func = getattr(self, '_validate_{}'.format(column), None)
            if value and validate_func:
                flag, new_value = validate_func(value)
                if flag:
                    value = new_value
                else:
                    errors = index, col, new_value
            d[column] = value

            #忽略空行
            if column == 'title' and not value:
                return -1

        if errors:
            return errors

        content = objs['content']
        detail = objs[self.content_type_obj.model_name]
        extend = objs['contentextend']
        obj = self.C.get(content['id'])
        if not obj:
            content['content_type'] = self.content_type_obj.id
            content['creator'] = request.user.id
            content['uuid'] = get_uuid()
            obj = self.C(**content)
            obj.save()

            detail_obj = self.D(content_id=obj.id, **detail)
            detail_obj.save()

            extend_obj = self.E(content_id=obj.id, **extend)
            extend_obj.save()
        else:
            if content['title']:
                obj.update(**content)
                obj.save()

                detail_obj = obj.get_detail()
                detail_obj.update(**detail)
                detail_obj.save()

                extend_obj = obj.get_content()
                extend_obj.update(**extend)
                extend_obj.save()

        return errors


    def view(self, id):
        from uliweb.utils.timesince import timesince

        obj = self.C.get(int(id))
        detail = obj.get_detail()
        extend = obj.get_content()

        def _convert_labels(value, o):
            s = []
            if obj.category:
                s.append(u'<span class="label label-default">{}</span>'.format(
                    self.C.category.get_display_value(obj.category)))
            if detail.domain:
                s.append(u'<span class="label label-success">{}</span>'.format(
                    self.D.domain.get_display_value(detail.domain)))
            if detail.source:
                s.append(u'<span class="label label-warning">{}</span>'.format(
                    self.D.source.get_display_value(detail.source)))
            if detail.priority:
                s.append(u'<span class="label label-info">{}</span>'.format(
                    self.D.priority.get_display_value(detail.priority)))
            return ' '.join(s)

        return {
                'title': obj.title,
                'object': detail,
                'content': extend.content,
                'summary': extend.summary,
                'memo': extend.memo,
                'status': self.D.status.get_display_value(detail.status),
                'time': '{} / {}'.format(detail.plan_begin_date or '-', detail.plan_finish_date or '-'),
                'responsible': u(detail.responsible or ''),
                'page_num': detail.page_num,
                'trans_num': detail.trans_num,
                'batch_num': detail.batch_num,
                'key': obj.uuid,
                'creator': u(obj.creator),
                'created_time': timesince(obj.created_time),
                'milestone': u(detail.milestone),
                'submitter': u(detail.submitter),
                'in_task_list': detail.in_task_list,
                }

    def kanban(self):
        User = functions.get_model('user')
        Milestone = functions.get_model('milestone')

        users = User.get_choices()
        return {'domains':functions.get_parameter('domain'),
                'users':users,
                'milestones': Milestone.get_choices()
                }

    def _get_card_info(self, row):
        User = functions.get_model('user')

        card = {}

        card['id'] = row.content_id
        card['title'] = row.get_content().title
        card['user'] = u(row.responsible or '未指派')
        if row.responsible:
            card['avater'] = row.responsible.get_image_url()
        else:
            card['avater'] = User.get_default_image_url()
        card['url'] = '/issue/view/{}'.format(row.content_id)
        card['status'] = row.status or '01'

        return card

    def get_data(self):
        """
        获得某个领域的需求信息
        """
        domain = request.GET.get('domain')
        user = request.GET.get('user')
        milestone = request.GET.get('milestone')
        result = []
        status = {}
        for s in functions.get_parameter('issue_status'):
            status[s[0]] = x = {'name': s[0], 'title': s[1], 'items': []}
            result.append(x)
        for row in self.D.get_data(domain=domain,
                                   user=user,
                                   milestone=milestone,
                                   condition=self.C.c.deleted==False).order_by(self.C.c.modified_time.desc()):
            d = self._get_card_info(row)
            items = status[d['status']]['items']
            items.append(d)

        return json({'success':True, 'data':result})

    def change_status(self, issue_id):
        status = request.GET.get('status')

        obj = self.C.get(issue_id)
        detail = obj.get_detail()
        detail.status = status
        detail.save()

        return json({'success':True})