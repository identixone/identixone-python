class Notifications(object):

    def __init__(self, http_client):
        self.http_client = http_client

    def list(self, **kwargs):
        return self.http_client.get(
            'v1/settings/notifications/', params=kwargs)

    def create(self, name, is_active, transport, destination_url=None,
               conf_thresholds=None, age_from=None, age_to=None, sex=None,
               moods=None, liveness=None, sources=None,
               http_method=None):
        data = {
            'name': name,
            'is_active': is_active,
            'transport': transport,
            'destination_url': destination_url,
            'conf_thresholds': conf_thresholds,
            'age_from': age_from,
            'age_to': age_to,
            'sex': sex,
            'moods': moods,
            'liveness': liveness,
            'sources': sources,
            'http_method': http_method
        }
        return self.http_client.post('v1/settings/notifications/', data=data)

    def get(self, notification_id):
        return self.http_client.get(
            'v1/settings/notifications/{}/'.format(notification_id))

    def update(self, notification_id, **kwargs):
        return self.http_client.patch(
            'v1/settings/notifications/{}/'.format(notification_id),
            data=kwargs)

    def delete(self, notification_id):
        return self.http_client.delete(
            'v1/settings/notifications/{}/'.format(notification_id))
