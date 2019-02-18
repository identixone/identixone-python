class Records(object):

    def __init__(self, http_client):
        self.http_client = http_client

    def list(self, **kwargs):
        # Possible query params:
        #   period_start, period_end, pgn_start, qty,
        #   source, new, reinit, exact, ha, junk, nm, det
        boolean = ['new', 'reinit', 'exact', 'ha', 'junk', 'nm', 'det']
        for k, v in kwargs.items():
            if k in boolean:
                kwargs[k] = str(v).lower()
        return self.http_client.get('v1/records/', params=kwargs)

    def get(self, idxid, **kwargs):
        return self.http_client.get(
            'v1/records/{}/'.format(idxid), params=kwargs)

    def entry_delete(self, entry_id):
        return self.http_client.delete('v1/records/entry/{}/'.format(entry_id))
