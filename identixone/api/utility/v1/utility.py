from identixone.base.choices import Conf


class Utility(object):

    def __init__(self, http_client):
        self.http_client = http_client

    def asm(self, photo):
        files = {'photo': photo}
        return self.http_client.post('v1/utility/asm/', files=files)

    def liveness(self, photo):
        files = {'photo': photo}
        return self.http_client.post('v1/utility/liveness/', files=files)

    def compare(self, photo1, photo2,
                liveness_photo1=False, liveness_photo2=False, conf=Conf.HA):
        files = {'photo1': photo1, 'photo2': photo2}
        data = {
            'liveness_photo1': liveness_photo1,
            'liveness_photo2': liveness_photo2,
            'conf': conf
        }
        return self.http_client.post(
            'v1/utility/compare/', files=files, data=data)

    def customer(self, source, offset=10):
        params = {'source': source, 'offset': offset}
        return self.http_client.get('v1/utility/customer/', params=params)
