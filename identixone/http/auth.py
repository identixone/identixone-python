from requests.auth import AuthBase


class IdentixOneAuth(AuthBase):
    """Attaches Authorization header w/ token to the given Request object."""
    PREFIX = 'Token'

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = '{} {}'.format(self.PREFIX, self.token)
        return r
