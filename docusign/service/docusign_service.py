from docusign.service.token_service import DocusignTokenService


class DocusignService(DocusignTokenService):
    params = dict()

    def __init__(self, environment="dev", encoded_keys=None):
        super().__init__(environment, encoded_keys)
