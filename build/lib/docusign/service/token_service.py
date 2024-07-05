import datetime
import os
from docusign.exception import DocusignException, ErrorCodes
from docusign.helper.token import get_token, update_token
from docusign.service.http_service import HttpService


class DocusignTokenService(HttpService):
    API_DEV_URL = 'https://account-d.docusign.com'
    API_PROD_URL = 'https://account.docusign.com'
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*'
    }

    def __init__(self, environment="dev", encoded_keys=None, code_from_url=None):
        self.environment = os.environ.get('DOCUSIGN_ENV', environment)
        self.encoded_keys = os.environ.get('DOCUSIGN_ENCODED_KEYS', encoded_keys)
        self.code_from_url = os.environ.get('DOCUSIGN_CODE_FROM_URL', code_from_url)
        if self.environment is None:
            raise ValueError(ErrorCodes.ENVIRONMENT_ERROR)
        api_url = self.API_DEV_URL if self.environment == 'dev' else self.API_PROD_URL
        super().__init__(api_url)
        self.token_dict = get_token()

        if self.token_dict is None:
            if self.encoded_keys is None:
                raise ValueError(ErrorCodes.ENCODED_KEYS_ERROR)
            self.headers['Authorization'] = f'Basic {self.encoded_keys}'
            if self.code_from_url is None:
                raise ValueError(ErrorCodes.CODE_FROM_URL_ERROR)
            payloads = dict(code=self.code_from_url, grant_type='authorization_code')
            self.token_dict = self.retrieve_access_token(payloads)
            return
        self.headers['Authorization'] = f'Bearer {self.token_dict["access_token"]}'
        if datetime.datetime.now() < datetime.datetime.now() + datetime.timedelta(
                seconds=int(self.token_dict['expires_in'])):
            return
        payloads = dict(refresh_token=self.token_dict['refresh_token'], grant_type='refresh_token')
        self.token_dict = self.retrieve_access_token(payloads)

    def retrieve_access_token(self, payloads):
        res = self.connect('POST', '/oauth/token', payloads, self.headers)
        update_token(res)
        return res
