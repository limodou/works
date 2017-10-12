#coding=utf8

from uliweb import expose, functions
from uliweb.utils.common import safe_str

@expose('/uploadfiles')
class UploadFilesView(functions.MultiView):
    def _save_file(self, key):
        F = functions.get_model('uploadfiles')
        path = 'files/{}'.format(key)
        obj = F.save_request_file(key, path, memo='', file_fieldname='upload')
        return json({'uploaded': 1, 'fileName': obj.filename,
                     'url': functions.get_href(obj.filename_path)+'?alt='+safe_str(obj.filename)
                     })

    def upload_image(self):
        key = request.GET.get('key')
        return self._save_file(key)

    def upload_file(self):
        key = request.GET.get('key')
        return self._save_file(key)
