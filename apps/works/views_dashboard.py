#coding=utf-8
# 个人面板

from uliweb import functions, expose

@expose('/<username>')
class DashBoard(object):
    @expose('')
    def index(self, username):
        User = functions.get_model('user')
        user = User.get(User.c.username==username)
        if not user:
            error('{}用户不存在'.format(username))

        return {'user':user}