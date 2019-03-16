class IdentixOneException(Exception):
    """Base for all errors produced by this library"""
    pass


class ImproperlyConfigured(IdentixOneException):
    """Errors that occur during configuration of Client"""
    pass
