import os
import sys

from docusign.serializer import Serializer

ROOT_DIR = os.path.split(os.environ['VIRTUAL_ENV'])[0] if 'VIRTUAL_ENV' in os.environ else sys.path[1]

file_path = f'{ROOT_DIR}/docusign_tokens_json'


def get_token(path=None):
    try:
        with open(file_path if path is None else path, "r") as file:
            token_dict = Serializer.load(file)
            file.close()
            return token_dict
    except Exception as e:
        return None


def update_token(token, path=None):
    try:
        with open(file_path if path is None else path, "wb") as file:
            file.write(Serializer.dumps(token))
            file.close()
    except Exception as e:
        return None
