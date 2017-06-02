#coding=utf8

from uliweb import expose, functions

@expose('/uploadfiles')
class UploadFilesView(functions.MultiView):
    def upload_image(self):
        F = functions.get_model('uploadfiles')
        key = request.GET.get('key')
        path = 'files/{}'.format(key)
        obj = F.save_request_file(key, path, memo='', file_fieldname='upload')
        return json({'uploaded': 1, 'fileName': obj.filename,
                     'url': functions.get_href(obj.filename_path)})

    def upload_file(self, content_id):
        return self.upload_image(content_id)
