from identixone.utils.decorators import deprecated


class Records(object):

    def __init__(self, http_client):
        self.http_client = http_client

    @deprecated(deadline_date='12:00 UTC, 15 June 2019',
                msg='Use Entries.list instead. Also see stats endpoints.')
    def list(self, **kwargs):
        # Possible query params:
        #   period_start, period_end, pgn_start, qty,
        #   source, new, reinit, exact, ha, junk, nm, det
        boolean = ['new', 'reinit', 'exact', 'ha', 'junk', 'nm', 'det']
        for k, v in kwargs.items():
            if k in boolean:
                kwargs[k] = str(v).lower()
        return self.http_client.get('v1/records/', params=kwargs)

    @deprecated(deadline_date='12:00 UTC, 15 June 2019',
                msg='Use Entries.list with idxid param instead.')
    def get(self, idxid, **kwargs):
        return self.http_client.get(
            'v1/records/{}/'.format(idxid), params=kwargs)

    @deprecated(deadline_date='12:00 UTC, 15 June 2019',
                msg='Use client.entries.delete instead.')
    def entry_delete(self, entry_id):
        return self.http_client.delete('v1/records/entry/{}/'.format(entry_id))
