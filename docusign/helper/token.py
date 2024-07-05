import os
import sys

from docusign.exception import DocusignException
from docusign.serializer import Serializer

ROOT_DIR = os.path.split(os.environ['VIRTUAL_ENV'])[0] if 'VIRTUAL_ENV' in os.environ else sys.path[1]

file_path = f'{ROOT_DIR}/docusign_tokens_json'


def get_token():
    try:
        with open(file_path, "r") as file:
            token_dict = Serializer.load(file)
            file.close()
            return token_dict
    except Exception as e:
        return None


def update_token(token):
    try:
        with open(file_path, "wb") as file:
            file.write(Serializer.dumps(token))
            file.close()
    except Exception as e:
        return None