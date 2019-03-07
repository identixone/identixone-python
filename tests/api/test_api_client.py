import unittest
import uuid
import os

from identixone.api.client import Client
from identixone.base.exceptions import IdentixOneException


class TestAPIClient(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.token = uuid.uuid4().hex
        super(TestAPIClient, self).__init__(*args, **kwargs)

    def test_unsupported_version_raises_exception(self):
        with self.assertRaises(IdentixOneException):
            Client(token=self.token, version=None)

    def test_no_version_raises_exception(self):
        with self.assertRaises(IdentixOneException):
            Client(token=self.token, version=9999)

    def test_no_token_raises_exception(self):
        with self.assertRaises(IdentixOneException):
            Client(token=None, version=1)

    def test_token_get_from_environ(self):
        os.environ['IDENTIXONE_TOKEN'] = '123lskdfjldksjf123'
        client = Client(version='1')
        self.assertEqual(client.token, '123lskdfjldksjf123')
    
    def test_version_get_from_environ(self):
        os.environ['IDENTIXONE_VERSION'] = '1'
        client = Client(token='adflsdkfjsakldfj')
        self.assertEqual(client.version, '1')
