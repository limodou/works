#coding=utf-8

from uliweb import functions

def get_content_type(name):
    """
    根据name获取对应的content_type对象
    :param name:
    :return:
    """
    ContentType = functions.get_model('contenttype')
    content_type = ContentType.get(ContentType.c.name == name)
    return content_type
