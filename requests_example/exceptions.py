class BaseException(Exception):
    pass


class ClientConnectionError(BaseException):
    pass


class ClientError(BaseException):
    pass


class ServerError(BaseException):
    pass
