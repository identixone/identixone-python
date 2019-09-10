class PersonsLists:

    def __init__(self, http_client):
        self.http_client = http_client

    def create(self, name):
        data = {'name': name}
        return self.http_client.post('v1/lists/persons/', data=data)

    def list(self, **kwargs):
        return self.http_client.get('v1/lists/persons/', params=kwargs)

    def get(self, pl_id):
        return self.http_client.get('v1/lists/persons/{}/'.format(pl_id))

    def update(self, pl_id, name):
        data = {'name': name}
        return self.http_client.patch('v1/lists/persons/{}/'.format(pl_id), data=data)

    def delete(self, pl_id):
        return self.http_client.delete('v1/lists/persons/{}/'.format(pl_id))

    def idxids_list(self, pl_id):
        return self.http_client.get('v1/lists/persons/{}/idxids/'.format(pl_id))

    def create_idxids(self, pl_id, idxids):
        data = {'idxids': idxids}
        return self.http_client.post('v1/lists/persons/{}/idxids/'.format(pl_id), data=data)

    def delete_idxids(self, pl_id, idxids):
        data = {'idxids': idxids}
        return self.http_client.delete('v1/lists/persons/{}/idxids/'.format(pl_id), data=data)

    def exended_idxids_list(self, pl_id, idxids):
        data = {'idxids': idxids}
        return self.http_client.get('v1/lists/persons/{}/idxids/extended/'.format(pl_id), data)

    def delete_idxids_in_lists(self, list_ids, idxids):
        data = {
            'list_ids': list_ids,
            'idxids': idxids
        }
        return self.http_client.delete('v1/lists/persons/idxids/', data=data)

    def create_idxids_in_lists(self, list_ids, idxids):
        data = {
            'list_ids': list_ids,
            'idxids': idxids
        }
        return self.http_client.post('v1/lists/persons/idxids/', data=data)

    def delete_all_idxids(self, idxid):
        return self.http_client.delete('v1/lists/persons/{}/idxids/all/'.format(idxid))

    def delete_idxid_from_lists(self, list_ids, idxid):
        data = {'lists_ids': list_ids}
        return self.http_client.post('v1/lists/persons/idxids/{}/'.format(idxid), data=data)

    def delete_idxid_from_all_lists(self, idxid):
        return self.http_client.post('v1/lists/persons/idxids/{}/all/'.format(idxid))
