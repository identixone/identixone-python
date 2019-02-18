import unittest
import uuid

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
