class Auth(object):

    def __init__(self, http_client):
        self.http_client = http_client

    def create_token(self, permanent=False):
        if permanent:
            url = 'v1/login/permanent/'
        else:
            url = 'v1/login/'
        return self.http_client.post(url)
