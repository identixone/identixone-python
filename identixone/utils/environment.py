ENV_BASE_PREFIX = 'IDENTIXONE_'


def env_var(environment, name):
    try:
        return environment.get('{}{}'.format(ENV_BASE_PREFIX, name), None)
    except Exception as e:
        # TODO: custom exc
        raise RuntimeError('Invalid environment', e)
