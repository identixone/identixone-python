class Entries(object):

    def __init__(self, http_client):
        self.http_client = http_client

    def list(self, **kwargs):
        return self.http_client.get('v1/entries/', params=kwargs)

    def delete(self, id):
        return self.http_client.delete('v1/entries/{}/'.format(id))

    def stats_idxid(self, idxid):
        return self.http_client.get('v1/entries/stats/idxid/{}/'.format(idxid))

    def stats_sources(self, **kwargs):
        return self.http_client.get('v1/entries/stats/sources/', params=kwargs)
