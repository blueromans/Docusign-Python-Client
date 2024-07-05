class ErrorCodes:
    CODE_FROM_URL_ERROR = 'Code from url error!'
    INVALID_ATTRIBUTE = 'Invalid attribute!'
    ENVIRONMENT_ERROR = 'Invalid environment!'
    TOKEN_ERROR = 'Invalid token!'
    ENCODED_KEYS_ERROR = 'Invalid encoded keys!'
    API_KEY_ERROR = 'Invalid api key!'
    API_URL_ERROR = 'Invalid api url!'


class DocusignException(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message
