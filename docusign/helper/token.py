import os
import sys

from docusign.serializer import Serializer

ROOT_DIR = os.path.split(os.environ['VIRTUAL_ENV'])[0] if 'VIRTUAL_ENV' in os.environ else sys.path[1]

file_path = f'{ROOT_DIR}/docusign_tokens_json'


def get_token(path=None):
    file_path_ = file_path if path is None else path
    if not os.path.isfile(file_path_):
        return None
    file = open(file_path_, "r")
    token_dict = Serializer.load(file)
    file.close()
    return token_dict


def update_token(token, path=None):
    file_path_ = file_path if path is None else path
    if not os.path.isfile(file_path_):
        return None
    file = open(file_path_, "wb")
    file.write(Serializer.dumps(token))
    file.close()
