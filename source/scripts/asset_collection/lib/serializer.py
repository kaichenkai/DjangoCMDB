# -*- coding:utf-8 -*-
import json
from json.encoder import JSONEncoder
from .response import BaseResponse


class JsonEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, BaseResponse):
            return o.__dict__
        return JSONEncoder.default(self, o)


class Json(object):
    @staticmethod
    def dumps(response, ensure_ascii=False):
        headers = json.dumps(response, ensure_ascii=ensure_ascii, cls=JsonEncoder)
        return headers
