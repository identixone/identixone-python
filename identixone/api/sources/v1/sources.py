from identixone.base.choices import Conf


class Sources(object):

    def __init__(self, http_client):
        self.http_client = http_client

    def list(self, **kwargs):
        return self.http_client.get('v1/sources/', params=kwargs)

    def get(self, source_id):
        return self.http_client.get('v1/sources/{}/'.format(source_id))

    def create(self, name, pps_timestamp=False,
               identify_facesize_threshold=None, auto_create_persons=False,
               auto_create_facesize_threshold=None, auto_create_on_ha=False,
               auto_create_on_junk=False, auto_check_face_angle=True,
               auto_check_angle_threshold=None, auto_check_asm=True,
               auto_create_check_blur=True, auto_create_check_exp=True,
               auto_check_liveness=False, auto_create_liveness_only=False,
               manual_create_facesize_threshold=None,
               manual_create_on_ha=False, manual_create_on_junk=False,
               manual_check_asm=True, manual_create_liveness_only=False,
               manual_check_liveness=False,
               store_images_for_confs=[
                   Conf.NEW, Conf.EXACT, Conf.HA, Conf.JUNK,
                   Conf.NM, Conf.DET, Conf.REINIT]):
        data = {
            'name': name,
            'pps_timestamp': pps_timestamp,
            'identify_facesize_threshold': identify_facesize_threshold,
            'auto_create_persons': auto_create_persons,
            'auto_create_facesize_threshold': auto_create_facesize_threshold,
            'auto_create_on_ha': auto_create_on_ha,
            'auto_create_on_junk': auto_create_on_junk,
            'auto_check_face_angle': auto_check_face_angle,
            'auto_check_angle_threshold': auto_check_angle_threshold,
            'auto_check_asm': auto_check_asm,
            'auto_create_check_blur': auto_create_check_blur,
            'auto_create_check_exp': auto_create_check_exp,
            'auto_check_liveness': auto_check_liveness,
            'auto_create_liveness_only': auto_create_liveness_only,
            'manual_create_facesize_threshold': manual_create_facesize_threshold,  # noqa: E501
            'manual_create_on_ha': manual_create_on_ha,
            'manual_create_on_junk': manual_create_on_junk,
            'manual_check_asm': manual_check_asm,
            'manual_create_liveness_only': manual_create_liveness_only,
            'manual_check_liveness': manual_check_liveness,
            'store_images_for_confs': store_images_for_confs
        }
        return self.http_client.post('v1/sources/', data=data)

    def update(self, source_id, **kwargs):
        return self.http_client.patch(
            'v1/sources/{}/'.format(source_id), data=kwargs)

    def delete(self, source_id):
        return self.http_client.delete('v1/sources/{}/'.format(source_id))
