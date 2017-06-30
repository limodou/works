#coding=utf8
# 解析业务功能表

from uliweb import functions
from uliweb.utils.sorteddict import SortedDict
from uliweb.utils.textconvert import text2html
from openpyxl import load_workbook
import logging

log = logging.getLogger(__name__)

class Reader(object):
    """
    用于某个Sheet数据的装入
    """
    def __init__(self, wb, begin=1, verbose=True):
        """
        :param wb: wookbook
        :param sheetname: sheet名
        :param begin: 起始行数
        """
        self.wb = wb
        self.begin = begin
        self.verbose = verbose
        self.reqs = SortedDict()

    def read(self):
        sheet = self.wb[u'业务规则']
        for i, row in enumerate(sheet.rows):
            if i < self.begin:
                continue
            r = self.reqs.setdefault(row[0].value, [])
            r.append(row[3].value)

        C = functions.get_model('content')
        for k, v in self.reqs.items():
            obj = C.get(C.c.title==k)
            if not obj:
                print u'!!!!!! Not found for "{}"'.format(k)
            else:
                extend = obj.get_content()
                extend.content = text2html('\n'.join(v))
                extend.save()


def call(args, options, global_options):
    if len(args) != 2:
        print 'Usage: uliweb call {} filename'.format(args[0])
        return

    wb = load_workbook(args[1], read_only=True)
    reader = Reader(wb)
    reader.read()
