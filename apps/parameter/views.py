#coding=utf-8
from uliweb import expose, functions

@expose('/settings/parameter')
class ParameterView(functions.MultiView):
    def __init__(self):
        self.PV = functions.get_model('parametervalues')
        self.P = functions.get_model('parameter')

    @expose('')
    def list(self):
        parameter = request.GET.get('parameter')
        condition = self.PV.c.parameter==parameter

        return self._list(self.PV,
                          condition=condition,
                          order_by=self.PV.c.order)

    def add(self):
        """
        增加参数取值
        :return:
        """
        parameter = request.GET.get('parameter')

        def pre_save(data):
            data['parameter'] = int(parameter)

        return self._add(self.PV,
                         pre_save=pre_save,
                         layout_class='bs3t',
                         form_args={'action':url_for(self.add, parameter=parameter)},
                         json_result=True)

    def edit(self, id):
        """
        增加参数取值
        :return:
        """

        obj = self.PV.get(int(id))
        return self._edit(self.PV,
                         obj=obj,
                         layout_class='bs3t',
                         # form_args={'action':url_for(self.edit, id=id)},
                         json_result=True)

    def delete(self, id):
        obj = self.PV.get(id)
        return self._delete(self.PV,
                            obj=obj,
                            json_result=True)

    def get_parameters(self):
        """
        分类返回
        :return:
        """
        return self._list(self.P)

    def add_category(self):
        return self._add(self.P,
                         layout_class='bs3t',
                         json_result=True)
