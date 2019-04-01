import os
import inspect

from importlib import import_module

from identixone.base.exceptions import ImproperlyConfigured
from identixone.http.client import IdentixOneHttpClient
from identixone.utils import constants
from identixone.utils.environment import env_var


class Client(object):
    """
    High-level client to interact with the Identix.one API.
    """

    def __init__(self, token=None, version=None,
                 http_client=None, environment=None):
        """
        Initialize Client with credentials and optional http client.

        :param token: Access token to the Identix.one API
        :param version: Version of the API to use
        :param http_client: Class of http client to use for making requests
        :param environment: Environment from which to read config variables
        """
        self.environment = environment or os.environ
        self.token = token or self.env_var('TOKEN')

        self.version = str(version) if version else self.env_var('VERSION')
        if not self.version:
            raise ImproperlyConfigured(
                'Version must be provided. Valid choices are: {}'.format(
                    str(constants.SUPPORTED_API_VERSIONS)))

        if self.version not in constants.SUPPORTED_API_VERSIONS:
            raise ImproperlyConfigured(
                'Invalid version. Valid choices are: {}'.format(
                    str(constants.SUPPORTED_API_VERSIONS)))

        if not self.token:
            raise ImproperlyConfigured('API token must be provided.')

        if http_client:
            if not inspect.isclass(http_client):
                raise ImproperlyConfigured(
                        'Variable http_client has to be class type')
            self.http_client = http_client(auth_token=self.token)
        else:
            self.http_client = IdentixOneHttpClient(auth_token=self.token)

    def dynamic_import(self, module_path, attribute):
        """
        Imports any attribute from the module specified as string dotted path.
        Takes into account current supplied version to the Client instance.

        :param module_path: dotted path of the module from which to import from
        :param attribute: function, class or any other attr to be imported
        :return: imported attribute
        """
        version_str = 'v{}'.format(self.version)
        abs_path = '{}.{}'.format(module_path, version_str)
        module_object = import_module(abs_path)
        return getattr(module_object, attribute)

    def env_var(self, name):
        """
        Wrapper around env_var utility function with supplied current environ.

        :param name: name of the environment variable
        :return: value of the environment variable or None if it doesn't exist
        """
        return env_var(self.environment, name)

    @property
    def auth(self):
        cls = self.dynamic_import('identixone.api.auth', 'Auth')
        return cls(self.http_client)

    @property
    def entries(self):
        cls = self.dynamic_import('identixone.api.entries', 'Entries')
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
