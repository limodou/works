#coding=utf-8
from uliweb import expose, functions

@expose('/article')
class ArticleView(functions.MultiView):
    content_type = 'article'

    def __begin__(self):
        return functions.require_login()

    def __init__(self):
        #获取issue 内容类型对象
        self.content_type_obj = functions.get_content_type(self.content_type)

        self.C = functions.get_model('content') #主表
        self.D = functions.get_model(self.content_type_obj.model_name) #明细表
        self.E = functions.get_model('contentextend') #扩展表

    def _get_query_view(self):
        from uliweb_layout.form.query_view import QueryView
        from uliweb.utils.generic import ReferenceSelectField

        QueryForm = functions.get_form('QueryForm')
        User = functions.get_model('user')

        creator = ReferenceSelectField('user', query=User.all().order_by(User.c.username.asc()))

        fields = [
            {'name': 'title', 'type':'str', 'label':'标题/ID:'},
            {'name': 'category', 'type':'select', 'multiple': True, 'label':'分类:',
                'choices':functions.get_parameter('article_category')},
            {'name': 'creator', 'choices':creator.get_choices(), 'type':'select', 'label':'作者'},
        ]
        layout = [
            ['title', 'creator', 'category'],
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

    def _convert_title(self, value, obj):
        return value

    def _convert_created_time(self, value, obj):
        from uliweb.utils.timesince import timesince

        return timesince(obj['created_time'])

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
        if c.get('creator'):
            condition = (self.D.c.creator==c['creator']) & condition

        def content_title(value, obj):
            return value

        def content_created_time(value, obj):
            from uliweb.utils.timesince import timesince

            return timesince(obj['content.created_time'])

        return self._get_list(queryview=query,
                              queryform=query.get_json(),
                              condition=condition,
                              fields_convert_map={'content.title':content_title,
                                                  'content.created_time':content_created_time})

    def add(self):
        """
        增加新记录
        :return:
        """

        from uliweb.utils.common import get_uuid

        def get_form_field(name):
            from uliweb.form import TextField, StringField, SelectField

            if name == 'content':
                return TextField(u'内容')
            if name == 'title':
                return StringField(u'标题', required=True)
            if name == 'category':
                return SelectField(u'分类', choices=functions.get_parameter('article_category'))
            if name == 'uuid':
                return StringField()

        def pre_save(data):
            content = self.C(content_type=self.content_type_obj.id,
                             title=data['title'],
                             creator=request.user.id,
                             category=data['category'],
                             uuid=data['uuid'])
            content.save()
            data['content_id'] = content.id

        def post_save(obj, data):
            extend = self.E(content_id=obj.content_id,
                            content=data['content'])
            extend.save()

        def get_url(obj):
            return '/article/view/{}'.format(obj.content_id)

        uuid = get_uuid()
        data = {'uuid':uuid}

        return self._add(self.D,
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

            if name == 'content':
                return TextField(u'内容')
            if name == 'title':
                return StringField(u'标题', required=True)
            if name == 'category':
                return SelectField(u'分类', choices=functions.get_parameter('article_category'))


        def post_save(obj, data):
            content.update(title=data['title'], category=data['category'])
            r1 = content.save()

            extend.update(content=data['content'])
            r2 = extend.save()
            return r1 or r2

        data = {'title': content.title,
                'content': extend.content,
                'category': content.category}

        return self._edit(self.D,
                         obj=detail,
                         ok_url='/article/view/{}'.format(id),
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

    def view(self, id):
        from uliweb.utils.timesince import timesince

        obj = self.C.get(int(id))
        detail = obj.get_detail()
        extend = obj.get_content()

        return {
                'title': obj.title,
                'object': detail,
                'content_obj': obj,
                'content': extend.content,
                'uuid': obj.uuid,
                'creator': unicode(obj.creator),
                'created_time': timesince(obj.created_time),
                }

