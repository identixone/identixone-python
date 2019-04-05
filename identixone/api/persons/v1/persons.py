from identixone.base.choices import Conf


class Persons(object):

    def __init__(self, http_client):
        self.http_client = http_client

    def create(self, photo, source, facesize=None, asm=None, liveness=None,
               create_on_ha=False, create_on_junk=False,
               create_liveness_only=False):
        data = {
            'source': source,
            'facesize': facesize,
            'create_on_ha': create_on_ha,
            'create_on_junk': create_on_junk,
            'asm': asm,
            'liveness': liveness,
            'create_liveness_only': create_liveness_only
        }
        files = {'photo': photo}
        return self.http_client.post('v1/persons/', data=data, files=files)

    def entry(self, id, facesize=None, create_on_ha=False,
              create_on_junk=False):
        data = {
            'id': id,
            'facesize': facesize,
            'create_on_ha': create_on_ha,
            'create_on_junk': create_on_junk
        }
        return self.http_client.post('v1/persons/entry/', data=data)

    def search(self, photo, asm=None, liveness=None):
        data = {'asm': asm, 'liveness': liveness}
        files = {'photo': photo}
        return self.http_client.post(
            'v1/persons/search/', data=data, files=files)

    def reinit_image(self, idxid, photo, source, conf=Conf.HA, facesize=None,
                     liveness=None, reinit_liveness_only=False):
        data = {
            'source': source,
            'conf': conf,
            'facesize': facesize,
            'liveness': liveness,
            'reinit_liveness_only': reinit_liveness_only
        }
        files = {'photo': photo}
        return self.http_client.post(
            'v1/persons/reinit/{}/'.format(idxid), data=data, files=files)

    def reinit_id(self, id, facesize=None):
        data = {'id': id, 'facesize': facesize}
        return self.http_client.post('v1/persons/reinit/', data=data)

    def delete(self, idxid):
        return self.http_client.delete('v1/persons/{}/'.format(idxid))
