#coding=utf-8
from uliweb import expose, functions

@expose('/comment')
class CommentView(functions.MultiView):
    def __init__(self):
        self.C = functions.get_model('comment')
        self.D = functions.get_model('commentdetail')

    @expose('')
    def get(self):
        key = request.GET.get('index')
        obj = self.C.get(self.C.c.key==key)
        if not obj:
            return json({'success': True, 'count': 0, 'comments': []})
        else:
            comments = self._get_comments(obj)
            return json({'success': True, 'count': len(comments), 'comments':comments})

    def _get_comment(self, row):
        d = {}
        d['author'] = unicode(row.author)
        d['modified_time'] = row.modified_time.strftime('%Y-%m-%d %H:%M:%S')
        d['content'] = row.content
        d['avator'] = row.author.get_image_url()
        d['level'] = row.level
        d['order'] = row.order
        return d

    def _get_comments(self, obj):
        s = []
        for row in obj.comments.order_by(self.D.c.level, self.D.c.order):
            d = self._get_comment(row)
            s.append(d)

        return s

    def save(self):
        """
        保存评论

        需要在Query_string传参数：
            parent 表示回复的是哪条信息，目前没有用上
            index 表示对应的键值
        :return:
        """
        from uliweb.orm import do_, rawsql
        from sqlalchemy import select, func

        parent = request.GET.get('parent')
        index = request.GET.get('index')
        comment = self.C.get(self.C.c.key==index)
        if not comment:
            comment = self.C(key=index)
        comment.num += 1
        comment.save()

        max_order = do_(select([func.max(self.D.c.order)], self.C.c.key==index)).scalar() or 0
        obj = self.D(author=request.user.id, content=request.POST['content'],
                     comment=comment.id, level=1, order=max_order+1)
        obj.save()
        return json({'success': True, 'data': self._get_comment(obj)})
