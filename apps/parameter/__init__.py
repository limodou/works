#coding=utf-8

from uliweb import functions

def parameter_choices(name):
    from functools import partial

    return partial(get_parameter, name=name)

def get_parameter(name):
    from uliweb.utils.common import Serial
    from uliweb import settings
    from uliweb.orm import rawsql

    P = functions.get_model('parameter')
    PV = functions.get_model('parametervalues')
    cache = settings.get_var('PARAMETER/cache')
    timeout = settings.get_var('PARAMETER/timeout')

    def _db():
        para = P.get(P.c.name == name)
        if para:
            items = []
            for row in PV.filter(PV.c.parameter == para.id).order_by(PV.c.order):
                items.append((row.value, row.display))
            return items
        else:
            return []

    if cache:
        redis = functions.get_redis()
        result = None
        ##反序列化
        value = redis.get(name)
        if value:
            result = Serial.load(value)
        else:
            result = _db()
            ##序列化
            redis.setex(name, Serial.dump(result), timeout)
    else:
        result = _db()
    return result

def get_parameter_display(name, value):
    result = dict(get_parameter(name))
    return result.get(value, '')