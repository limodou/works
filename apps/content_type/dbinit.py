#coding=utf8
from uliweb import functions
from uliweb.i18n import ugettext_lazy as _

def init_content_type():
    ContentType = functions.get_model('contenttype')

    ct = [('issue', _('Request/Issue'), 'contentdetailissue'),
          ('article', _('Article'), 'contentdetailarticle')]

    for row in ct:
        name, display, model_name = row
        obj = ContentType.get(ContentType.c.name==name)
        if not obj:
            obj = ContentType(name=name, display=display, model_name=model_name)
            obj.save()

def init_parameter():
    Para = functions.get_model('parameter')

    paras = [
        ('issue_status', _('Status')),
        ('category', _('Category')),
        ('issue_priority', _('Priority')),
        ('issue_category', _('Category')),
        ('domain', _('Domain')),
        ('source', _('Source')),
        ('task_status', _('Status')),
        ('task_priority', _('Priority')),
        ('deploy', _('Deploy')),
        ('Article_category', _('Category')),
    ]
    for row in paras:
        name, display = row
        obj = Para.get(Para.c.name==name)
        if not obj:
            obj = Para(name=name, display=display)
            obj.save()

init_content_type()
init_parameter()