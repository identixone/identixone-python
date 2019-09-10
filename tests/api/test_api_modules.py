import json
import unittest
import uuid
import warnings

from requests import Response, Session
from unittest.mock import patch

from identixone.api.client import Client
from identixone.base.choices import (
    Conf, NotificationHTTPMethod, NotificationTransport)


class TestAPIModule(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.version = 1
        self.token = uuid.uuid4().hex
        self.client = Client('token', version=1)
        super(TestAPIModule, self).__init__(*args, **kwargs)

    @staticmethod
    def response(resp_body, status_code):
        response = Response()
        response.status_code = status_code
        response._content = json.dumps(resp_body).encode('utf-8')
        return response


class TestAPIAuthModule(TestAPIModule):

    @patch.object(Session, 'send')
    def test_create_temp_token(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)

        response = self.client.auth.create_token(permanent=False)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

        response = self.client.auth.create_token(permanent=True)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)


class TestAPINotificationsModule(TestAPIModule):

    @patch.object(Session, 'send')
    def test_list_notifications(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.notifications.list()
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_get_notifications(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.notifications.get(notification_id=1)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_create_notifications(self, mocked_send):
        status_code = 201
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.notifications.create(
            name='name', is_active=True,
            transport=NotificationTransport.WEBHOOK,
            http_method=NotificationHTTPMethod.GET,
            conf_thresholds=[Conf.EXACT, Conf.HA, Conf.JUNK],
            destination_url='https://api.identix.one/')
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_update_notifications(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.notifications.update(
            notification_id=1, is_active=False)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_delete_notifications(self, mocked_send):
        status_code = 204
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.notifications.delete(notification_id=1)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)


class TestAPIPersonsModule(TestAPIModule):

    @patch.object(Session, 'send')
    def test_create_persons_no_none_values_in_request(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.persons.create(photo='photo', source='source')
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

        sent_request_body = mocked_send.mock_calls[0][1][0].body.decode('utf-8')
        self.assertNotIn('name="asm"', sent_request_body)
        self.assertNotIn('name="liveness"', sent_request_body)
        self.assertNotIn('name="facesize"', sent_request_body)

    @patch.object(Session, 'send')
    def test_create_persons_fill_optional_values_in_request(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.persons.create(
            photo='photo', source='source',
            asm=True, liveness=True, facesize=25000)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

        sent_request_body = mocked_send.mock_calls[0][1][0].body.decode('utf-8')
        self.assertIn('name="asm"', sent_request_body)
        self.assertIn('name="liveness"', sent_request_body)
        self.assertIn('name="facesize"', sent_request_body)

    @patch.object(Session, 'send')
    def test_search_persons_no_none_values_in_request(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.persons.search(photo='photo')
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

        sent_request_body = mocked_send.mock_calls[0][1][0].body.decode('utf-8')
        self.assertNotIn('name="asm"', sent_request_body)
        self.assertNotIn('name="liveness"', sent_request_body)

    @patch.object(Session, 'send')
    def test_search_persons_fill_optional_values_in_request(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.persons.search(
            photo='photo', asm=True, liveness=True)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

        sent_request_body = mocked_send.mock_calls[0][1][0].body.decode('utf-8')
        self.assertIn('name="asm"', sent_request_body)
        self.assertIn('name="liveness"', sent_request_body)

    @patch.object(Session, 'send')
    def test_reinit_image_persons_no_none_values_in_request(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.persons.reinit_image(
            idxid='1', photo='photo', source='source', conf=Conf.EXACT)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

        sent_request_body = mocked_send.mock_calls[0][1][0].body.decode('utf-8')
        self.assertNotIn('name="facesize"', sent_request_body)
        self.assertNotIn('name="liveness"', sent_request_body)

    @patch.object(Session, 'send')
    def test_reinit_image_persons_fill_optional_values_in_request(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.persons.reinit_image(
            idxid='1', photo='photo', source='source', conf=Conf.EXACT,
            liveness=True, facesize=25000)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

        sent_request_body = mocked_send.mock_calls[0][1][0].body.decode('utf-8')
        self.assertIn('name="facesize"', sent_request_body)
        self.assertIn('name="liveness"', sent_request_body)

    @patch.object(Session, 'send')
    def test_reinit_id_persons(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.persons.reinit_id(id=1)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_delete_persons(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.persons.delete(idxid='1')
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_persons_entry(self, mocked_send):
        status_code = 201
        resp_body = {'idxid': str(uuid.uuid4())}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.persons.entry(id=1)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)


class TestAPIEntriesModule(TestAPIModule):

    @patch.object(Session, 'send')
    def test_list_entries(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.entries.list(
            conf='new,exact,ha', limit=10)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_stats_idxid(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.entries.stats_idxid(idxid='1')
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_stats_sources(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.entries.stats_sources(conf='new', limit=1000)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_delete_entry(self, mocked_send):
        status_code = 204
        resp_body = None
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.entries.delete(id=1)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)


class TestAPISourcesModule(TestAPIModule):

    @patch.object(Session, 'send')
    def test_list_sources(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.sources.list()
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_get_sources(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.sources.get(source_id=1)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_create_sources(self, mocked_send):
        status_code = 201
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.sources.create(name='name')
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_update_sources(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.sources.update(source_id=1, name='other')
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_delete_sources(self, mocked_send):
        status_code = 204
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.sources.delete(source_id=1)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)


class TestAPIUsersModule(TestAPIModule):

    @patch.object(Session, 'send')
    def test_users_me(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.users.me()
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_users_change_password_no_none_values_in_request(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.users.change_password(
            old_password='p', password='new_password', password2='new_password'
        )
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

        sent_request_body = mocked_send.mock_calls[0][1][0].body
        self.assertNotIn('reset_tokens', sent_request_body)

    @patch.object(Session, 'send')
    def test_users_change_password_reset_tokens_in_request(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.users.change_password(
            old_password='p', password='new_password',
            password2='new_password', reset_tokens=True
        )
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

        sent_request_body = mocked_send.mock_calls[0][1][0].body
        self.assertIn('reset_tokens', sent_request_body)

    @patch.object(Session, 'send')
    def test_users_list_tokens(self, mocked_send):
        status_code = 200
        resp_body = [{'key': 'value'}]
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.users.list_tokens(permanent=False)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

        resp_body = []
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.users.list_tokens(permanent=True)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

        resp_body = [{'key2': 'value2'}]
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.users.list_tokens()
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_users_bulk_delete_tokens(self, mocked_send):
        status_code = 204
        resp_body = None
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.users.bulk_delete()
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

        response = self.client.users.bulk_delete(permanent=False)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

        response = self.client.users.bulk_delete(permanent=True)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_users_get_tokens(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.users.get_token(id_or_token='id')
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_users_update_tokens(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.users.update_token(
            id_or_token='id', is_active=False)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_users_delete_tokens(self, mocked_send):
        status_code = 204
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.users.delete_token(id_or_token='id')
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)


class TestAPIUtilityModule(TestAPIModule):

    @patch.object(Session, 'send')
    def test_utility_asm(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.utility.asm(photo='photo')
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_utility_liveness(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.utility.liveness(photo='photo')
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_utility_compare(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.utility.compare(
            photo1='photo1', photo2='photo2', conf=Conf.JUNK)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_utility_customer(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.utility.customer(source='source', offset=20)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)


class TestAPIPersonListsModule(TestAPIModule):

    @patch.object(Session, 'send')
    def test_person_list_create(self, mocked_send):
        status_code = 201
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)

        response = self.client.persons_lists.create('test_name')
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_person_list_list(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)

        response = self.client.persons_lists.list()
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_person_list_get(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)

        response = self.client.persons_lists.get(32312123123)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_person_list_update(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)

        response = self.client.persons_lists.update(32432432, 'test_name_2')
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_person_list_delete(self, mocked_send):
        status_code = 204
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)

        response = self.client.persons_lists.delete(231232132)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_person_list_idxids_list(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)

        response = self.client.persons_lists.idxids_list(2344234324)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_person_list_create_idxids(self, mocked_send):
        status_code = 201
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        idxids = ['klsfjd39202', 'lksdfj23920']
        response = self.client.persons_lists.create_idxids(324324324, idxids)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_person_list_delete_idxids(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        idxids = ['klsfjd39202', 'lksdfj23920']
        response = self.client.persons_lists.delete_idxids(324324324, idxids)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_person_list_exended_idxids_list(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        idxids = ['klsfjd39202', 'lksdfj23920']
        response = self.client.persons_lists.exended_idxids_list(324324324, idxids)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_person_list_delete_idxids_in_lists(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        pl_ids = [324324324, 12321]
        idxids = ['klsfjd39202', 'lksdfj23920']
        response = self.client.persons_lists.delete_idxids_in_lists(pl_ids, idxids)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_person_list_create_idxids_in_lists(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        pl_ids = [324324324, 12321]
        idxids = ['klsfjd39202', 'lksdfj23920']
        response = self.client.persons_lists.create_idxids_in_lists(pl_ids, idxids)
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_person_list_delete_all_idxids(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.persons_lists.delete_all_idxids('dfdfklfgu34993')
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_person_list_delete_idxid_from_lists(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        pl_idx = [324324324, 12321]
        response = self.client.persons_lists.delete_idxid_from_lists(pl_idx, 'dfdfklfgu34993')
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)

    @patch.object(Session, 'send')
    def test_person_list_delete_idxid_from_all_lists(self, mocked_send):
        status_code = 200
        resp_body = {'key': 'value'}
        mocked_send.return_value = self.response(resp_body, status_code)
        response = self.client.persons_lists.delete_idxid_from_all_lists('dfdfklfgu34993')
        self.assertEqual(response.json(), resp_body)
        self.assertEqual(response.status_code, status_code)
