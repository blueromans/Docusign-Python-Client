import base64 as base64lib

import requests

from docusign.serializer import Serializer


class HttpService:
    REST_URL = None

    def __init__(self, REST_URL):
        self.REST_URL = REST_URL

    @staticmethod
    def parse_result(r, json=True, base64=False):
        if json is True:
            res = r.text.encode('utf-8')
            res = Serializer.loads(res)
            if r.status_code != 200 and r.status_code != 202:
                if 'error_description' in res:
                    raise ValueError(res['error_description'])
                if 'error' in res:
                    raise ValueError(res['error'])
            return res
        if base64 is True:
            return base64lib.b64encode(r.content).decode("utf-8")

    def post_request(self, url, request_body, headers, json=True, base64=False):
        r = requests.post(url, data=request_body, headers=headers)
        return self.parse_result(r, json, base64)

    def get_request(self, url, headers, json=True, base64=False):
        r = requests.get(url, headers=headers)
        return self.parse_result(r, json, base64)

    def connect(self, method, url, request_body={}, headers=None, json=True, base64=False):
        request_url = self.REST_URL + url if 'http' not in url and 'https' not in url else url
        if method == 'GET':
            return self.get_request(request_url, headers, json, base64)
        return self.post_request(request_url, request_body, headers, json, base64)
