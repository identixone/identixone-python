class Users(object):

    def __init__(self, http_client):
        self.http_client = http_client

    def me(self):
        return self.http_client.get('v1/users/me/')

    def change_password(self, password, password2, reset_tokens=None):
        data = {
            'password': password,
            'password2': password2,
            'reset_tokens': reset_tokens
        }
        return self.http_client.post('v1/users/password/change/', data=data)

    def list_tokens(self, permanent=None):
        params = None
        if permanent is not None:
            params = {'permanent': permanent}
        return self.http_client.get('v1/users/tokens/', params=params)

    def get_token(self, id_or_token):
        return self.http_client.get(
            'v1/users/tokens/{}/'.format(id_or_token))

    def update_token(self, id_or_token, **kwargs):
        return self.http_client.patch(
            'v1/users/tokens/{}/'.format(id_or_token), data=kwargs)

    def delete_token(self, id_or_token):
        return self.http_client.delete(
            'v1/users/tokens/{}/'.format(id_or_token))

    def bulk_delete(self, permanent=None):
        params = None
        if permanent is not None:
            params = {'permanent': permanent}
        return self.http_client.delete('v1/users/tokens/', params=params)
