#coding=utf-8
from uliweb import expose, functions

@expose('/settings/milestone')
class MilestoneView(functions.MultiView):
    def __init__(self):
        self.model = functions.get_model('milestone')

    @expose('')
    def list(self):
        return self._list(self.model)

    def add(self):
        return self._add(self.model,
                         layout_class='bs3t',
                         json_result=True)

    def edit(self, id):
        obj = self.model.get(id)

        return self._edit(self.model, obj=obj,
                          layout_class='bs3t',
                          json_result=True)

    def delete(self, id):
        obj = self.model.get(id)

        return self._delete(self.model, obj=obj)
