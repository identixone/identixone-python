import os
import unittest

from identixone.base.exceptions import ImproperlyConfigured
from identixone.utils.environment import env_var, ENV_BASE_PREFIX


class TestEnvironmentVar(unittest.TestCase):

    def test_os_environ_valid_var(self):
        key = 'KEY'
        value = 'VALUE'
        os.environ['{}{}'.format(ENV_BASE_PREFIX, key)] = value
        self.assertEqual(env_var(os.environ, key), value)

    def test_os_environ_invalid_without_prefix(self):
        key = 'KEY'
        value = 'VALUE'
        os.environ[key] = value
        self.assertIsNone(env_var(os.environ, key))

    def test_dict_environ_valid_var(self):
        environ = {}
        key = 'KEY'
        value = 'VALUE'
        environ['{}{}'.format(ENV_BASE_PREFIX, key)] = value
        self.assertEqual(env_var(environ, key), value)

    def test_dict_environ_invalid_without_prefix(self):
        environ = {}
        key = 'KEY'
        value = 'VALUE'
        environ[key] = value
        self.assertIsNone(env_var(os.environ, key))

    def test_invalid_environ_raises_exception(self):
        key = 'KEY'
        with self.assertRaises(ImproperlyConfigured):
            env_var([], key)
