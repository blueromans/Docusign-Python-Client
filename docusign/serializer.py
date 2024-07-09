import json


class Serializer(object):

    @staticmethod
    def dumps(data_obj):
        return json.dumps(data_obj, ensure_ascii=False,
                          allow_nan=False,
                          indent=None,
                          separators=(",", ":")).encode("utf-8")

    @staticmethod
    def loads(data_string):
        return json.loads(data_string)

    @staticmethod
    def load(file):
        return json.load(file)
