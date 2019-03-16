class NotificationTransport(object):
    WEBHOOK = 0
    WEBSOCKETS_CLIENT = 1
    WEBSOCKETS_SERVER = 2


class NotificationHTTPMethod(object):
    POST = 0
    GET = 1


class Conf(object):
    NEW = 'new'
    EXACT = 'exact'
    HA = 'ha'
    JUNK = 'junk'
    NM = 'nm'
    DET = 'det'
    REINIT = 'reinit'
