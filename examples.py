#!/usr/bin/env python
import datetime

from identixone.api import Client
from identixone.base.choices import (
    Conf, NotificationHTTPMethod, NotificationTransport)

token = 'token'
client = Client(token=token, version=1)


def list_records():
    period_start = datetime.datetime(year=2019, month=1, day=13, hour=19,
                                     minute=20, second=1)
    period_end = datetime.datetime(year=2019, month=1, day=22, hour=19,
                                   minute=20, second=1)
    r = client.records.list(new=True, nm=False, junk=False, exact=False,
                            ha=False, det=False, period_start=period_start,
                            period_end=period_end)
    print(r.json())


def sources_list():
    r = client.sources.list()
    print(r.json())


def sources_get():
    r = client.sources.get(source_id=1)
    print(r.json())


def sources_create():
    r = client.sources.create(name='source_name')
    print(r.json())


def sources_update():
    r = client.sources.update(source_id=1, name='source_name')
    print(r.json())


def sources_delete():
    r = client.sources.delete(source_id=1)
    print(r.status_code)


def utility_asm(photo):
    r = client.utility.asm(photo=photo)
    print(r.json())


def utility_liveness(photo):
    r = client.utility.liveness(photo=photo)
    print(r.json())


def utility_compare(photo1, photo2):
    r = client.utility.compare(
        photo1, photo2,
        liveness_photo1=False, liveness_photo2=False,
        conf=Conf.JUNK)
    print(r.json())


def utility_customer():
    r = client.utility.customer('source_name', offset=10)
    print(r.json())


def persons_create(photo):
    r = client.persons.create(photo=photo, source='source_name')
    print(r.json())


def persons_search(photo):
    r = client.persons.search(photo=photo)
    print(r.json())


def persons_reinit_image(photo):
    r = client.persons.reinit_image(
        idxid='idxid', photo=photo,
        source='source_name', conf=Conf.EXACT)
    print(r.json())


def persons_reinit_id():
    r = client.persons.reinit_id(id=1)
    print(r.json())


def persons_delete():
    r = client.persons.delete(idxid='idxid')
    print(r.json())


def get_token():
    r = client.users.get_token(token)
    print(r.json())


def update_token():
    r = client.users.update_token(token, is_active=True)
    print(r.json())
    r = client.users.update_token(token, is_active=False)
    print(r.json())


def delete_token():
    r = client.users.delete_token(token)
    print(r.json())


def bulk_delete_tokens():
    r = client.users.bulk_delete()
    print(r.status_code)


def bulk_delete_permanent_tokens():
    r = client.users.bulk_delete(permanent=True)
    print(r.status_code)


def bulk_delete_temporary_tokens():
    r = client.users.bulk_delete(permanent=False)
    print(r.status_code)


def idxid_records():
    idxid = 'idxid'
    r = client.records.get(idxid=idxid)
    print(r.json())


def entry_delete():
    entry_id = 1
    r = client.records.entry_delete(entry_id)
    print(r.status_code)


def auth_create_token():
    r = client.auth.create_token()
    print(r.json())


def auth_create_permanent_token():
    r = client.auth.create_permanent_token()
    print(r.json())


def list_notifications():
    r = client.notifications.list()
    print(r.json())


def delete_notifications():
    r = client.notifications.delete(notification_id=1)
    print(r.status_code)


def create_notifications():
    r = client.notifications.create(
        name='exact_and_ha', is_active=True,
        transport=NotificationTransport.WEBHOOK,
        http_method=NotificationHTTPMethod.POST,
        conf_thresholds=[Conf.EXACT, Conf.HA])
    print(r.json())


def update_notifications():
    r = client.notifications.update(notification_id=1, name='hello')
    print(r.json())


def create_token():
    r = client.auth.create_token(permanent=True)
    print(r.json())


def users_me():
    r = client.users.me()
    print(r.json())


def users_change_password():
    r = client.users.change_password('pwd', 'pwd', reset_tokens=False)
    print(r.json())


def users_list_tokens():
    r = client.users.list_tokens(permanent=True)
    print(r.json())
    r = client.users.list_tokens(permanent=False)
    print(r.json())
    r = client.users.list_tokens()
    print(r.json())


def users_get_token():
    r = client.users.get_token(token, permanent=True)
    print(r.json())


def users_update_token():
    r = client.users.update_token(token, is_active=False)
    print(r.json())
    r = client.users.update_token(token, is_active=True)
    print(r.json())


def users_delete_token():
    r = client.users.delete_token(token)
    print(r.json())
