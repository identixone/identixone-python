import platform
import uuid

from requests import Request, Session, hooks

from urllib.parse import urljoin

from identixone import __version__
from identixone.http.auth import IdentixOneAuth
from identixone.utils import constants


class IdentixOneHttpClient(object):
    """
    Http client used to make actual HTTP requests to Identix.one API.
    You can subclass it and provide new class as http_client param into Client.
    """

    def __init__(self, auth_token, request_hooks=None, timeout=None):
        self.auth = IdentixOneAuth(token=auth_token)
        self.session = Session()
        self.request_hooks = request_hooks or hooks.default_hooks()
        self.timeout = timeout or constants.HTTP_CLIENT_TIMEOUT
        self.base_url = constants.HTTP_CLIENT_BASE_URL

    @property
    def common_headers(self):
        return {
            'User-Agent': 'identixone-python/{} (Python {})'.format(
                __version__, platform.python_version()),
            'Request-ID': str(uuid.uuid4())
        }

    def get(self, url, params=None, data=None, files=None,
            headers=None, auth=None):
        return self.request(
            method='GET', url=url, params=params,
            data=data, files=files, headers=headers, auth=auth)

    def post(self, url, params=None, data=None, files=None,
             headers=None, auth=None):
        return self.request(
            method='POST', url=url, params=params,
            data=data, files=files, headers=headers, auth=auth)

    def patch(self, url, params=None, data=None, files=None,
              headers=None, auth=None):
        return self.request(
            method='PATCH', url=url, params=params,
            data=data, files=files, headers=headers, auth=auth)

    def delete(self, url, params=None, data=None, files=None,
               headers=None, auth=None):
        return self.request(
            method='DELETE', url=url, params=params,
            data=data, files=files, headers=headers, auth=auth)

    def request(self, method, url, params=None, data=None, files=None,
                headers=None, auth=None):
        method = method.upper()
        full_url = urljoin(self.base_url, url)
        headers = headers or {}
        headers.update(self.common_headers)

        if 'Accept' not in headers:
            headers['Accept'] = 'application/json'

        self.session.auth = auth or self.auth
        self.session.headers.update(headers)

        request = Request(**{
            'method': method,
            'url': full_url,
            'params': params,
            'data': data,
            'files': files,
            'headers': headers,
            'hooks': self.request_hooks
        })

        prepped_request = self.session.prepare_request(request)

        return self.session.send(
            prepped_request,
            allow_redirects=False,
            timeout=self.timeout,
        )
