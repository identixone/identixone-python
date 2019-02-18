import os

from importlib import import_module

from identixone.base.exceptions import IdentixOneException
from identixone.http.client import IdentixOneHttpClient
from identixone.utils import constants
from identixone.utils.environment import env_var


class Client(object):

    def __init__(self, token, version, http_client=None, environment=None):
        """
        Initialize Client with credentials and optional http client.
        """
        self.environment = environment or os.environ
        self.token = token or self.env_var('TOKEN')

        self.version = version or self.env_var('TOKEN')
        if not self.version:
            raise IdentixOneException(
                'Version must be provided. Valid choices are: {}'.format(
                    str(constants.SUPPORTED_API_VERSIONS)))

        if self.version not in constants.SUPPORTED_API_VERSIONS:
            raise IdentixOneException(
                'Invalid version. Valid choices are: {}'.format(
                    str(constants.SUPPORTED_API_VERSIONS)))

        if not self.token:
            raise IdentixOneException('API token must be provided.')

        self.http_client = http_client or IdentixOneHttpClient(
            auth_token=self.token)

    def dynamic_import(self, module_path, attribute):
        version_str = 'v{}'.format(self.version)
        abs_path = '{}.{}'.format(module_path, version_str)
        module_object = import_module(abs_path)
        return getattr(module_object, attribute)

    def env_var(self, name):
        return env_var(self.environment, name)

    @property
    def auth(self):
        cls = self.dynamic_import('identixone.api.auth', 'Auth')
        return cls(self.http_client)

    @property
    def notifications(self):
        cls = self.dynamic_import(
            'identixone.api.notifications', 'Notifications')
        return cls(self.http_client)

    @property
    def persons(self):
        cls = self.dynamic_import('identixone.api.persons', 'Persons')
        return cls(self.http_client)

    @property
    def records(self):
        cls = self.dynamic_import('identixone.api.records', 'Records')
        return cls(self.http_client)

    @property
    def sources(self):
        cls = self.dynamic_import('identixone.api.sources', 'Sources')
        return cls(self.http_client)

    @property
    def users(self):
        cls = self.dynamic_import('identixone.api.users', 'Users')
        return cls(self.http_client)

    @property
    def utility(self):
        cls = self.dynamic_import('identixone.api.utility', 'Utility')
        return cls(self.http_client)
