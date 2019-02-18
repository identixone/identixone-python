import unittest
import uuid

from requests import PreparedRequest, Response, Session
from unittest.mock import patch, Mock

from identixone.http.client import IdentixOneHttpClient


class TestHttpClientRequest(unittest.TestCase):

    def setUp(self):
        self.session_patch = patch('identixone.http.client.Session')

        self.request_mock = Mock(wraps=PreparedRequest())
        self.request_mock.headers = {}

        self.session_mock = Mock(wraps=Session())
        self.session_mock.prepare_request.return_value = self.request_mock
        self.session_mock.send.return_value = Response()
        self.session_mock.headers = {}

        session_constructor_mock = self.session_patch.start()
        session_constructor_mock.return_value = self.session_mock

        self.auth_token = uuid.uuid4().hex

        self.client = IdentixOneHttpClient(auth_token=self.auth_token)

    def tearDown(self):
        self.session_patch.stop()

    def test_request_sets_common_headers(self):
        self.client.request('method', 'URL')
        assert self.client.session.headers['User-Agent'].startswith(
            'identixone-python')
        self.assertIsNotNone(self.client.session.headers['Request-ID'])

    def test_set_accept_header_if_missing(self):
        self.client.request('method', 'URL')
        self.assertEqual(
            'application/json', self.client.session.headers['Accept'])

    def test_specify_accept_header_takes_effect(self):
        self.client.request('method', 'URL', headers={'Accept': 'text/html'})
        self.assertEqual('text/html', self.client.session.headers['Accept'])
