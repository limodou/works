#coding=utf-8
# 个人面板

from uliweb import functions, expose


def __begin__():
    return functions.require_login()

@expose('/dashboard')
class DashBoardView(object):

    @expose('')
    def index(self):
        return {}