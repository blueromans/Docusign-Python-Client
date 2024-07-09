from docusign.service.token_service import DocusignTokenService


class DsEnvelopeService(DocusignTokenService):
    params = dict()

    def __init__(self, environment="dev", encoded_keys=None, path=None, **kwargs):
        super().__init__(environment, encoded_keys, path)
        self.args = {
            "account_id": kwargs["account_id"],
            "base_path": kwargs["base_path"],
            "access_token": self.token_dict['access_token'],
        }

    def get_documents(self, envelope_id):
        headers = {
            'content-type': 'application/json',
            'accept': '*/*',
            'Authorization': f'Bearer {self.token_dict["access_token"]}'
        }
        url = f'{self.args["base_path"]}/v2.1/accounts/{self.args["account_id"]}/envelopes/{envelope_id}/documents'
        res = self.connect('GET', url, headers=headers)
        return res

    def get_document(self, uri):
        headers = {
            'content-type': 'application/json',
            'accept': '*/*',
            'Authorization': f'Bearer {self.token_dict["access_token"]}'
        }
        url = f'{self.args["base_path"]}/v2.1/accounts/{self.args["account_id"]}{uri}'
        res = self.connect('GET', url, headers=headers, json=False, base64=True)
        return res

