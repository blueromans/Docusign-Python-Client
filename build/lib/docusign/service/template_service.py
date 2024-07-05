from docusign_esign import EnvelopeDefinition, TemplateRole, EnvelopesApi

from docusign.helper.ds_client import create_api_client
from docusign.service.token_service import DocusignTokenService


class DsTemplateService(DocusignTokenService):
    params = dict()

    def __init__(self, environment="dev", encoded_keys=None, code_from_url=None, **kwargs):
        super().__init__(environment, encoded_keys, code_from_url)
        self.envelope_args = {
            "signer_email": kwargs['signer_email'],
            "signer_name": kwargs['signer_name'],
            "cc_email": kwargs['cc_email'],
            "cc_name": kwargs['cc_name'],
            "template_id": kwargs['template_id']
        }
        self.args = {
            "account_id": kwargs["ds_account_id"],
            "base_path": kwargs["ds_base_path"],
            "access_token": self.token_dict['access_token'],
            "envelope_args": self.envelope_args
        }

    def send_envelope(self):
        """
        1. Create the envelope request object
        2. Send the envelope
        """
        envelope_args = self.args["envelope_args"]
        # 1. Create the envelope request object
        envelope_definition = self.make_envelope(envelope_args)

        # 2. call Envelopes::create API method
        # Exceptions will be caught by the calling function
        api_client = create_api_client(base_path=self.args["base_path"], access_token=self.args["access_token"])
        envelope_api = EnvelopesApi(api_client)
        results = envelope_api.create_envelope(account_id=self.args["account_id"],
                                               envelope_definition=envelope_definition)
        envelope_id = results.envelope_id
        return {"envelope_id": envelope_id}

    # ds-snippet-end:eSign9Step3
    @classmethod
    def make_envelope(cls, args):
        """
        Creates envelope
        args -- parameters for the envelope:
        signer_email, signer_name, signer_client_id
        returns an envelope definition
        """

        # create the envelope definition
        envelope_definition = EnvelopeDefinition(
            status="sent",  # requests that the envelope be created and sent.
            template_id=args["template_id"]
        )
        # Create template role elements to connect the signer and cc recipients
        # to the template
        signer = TemplateRole(
            email=args["signer_email"],
            name=args["signer_name"],
            role_name="signer"
        )
        # Create a cc template role.
        cc = TemplateRole(
            email=args["cc_email"],
            name=args["cc_name"],
            role_name="cc"
        )

        # Add the TemplateRole objects to the envelope object
        envelope_definition.template_roles = [signer, cc]
        return envelope_definition