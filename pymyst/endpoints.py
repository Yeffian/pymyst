endpoints = {
    'base': 'https://paste.myst.rs/api/v2',
    'data': '/data',
    'time': '/time',
    'paste': '/paste',
    'user': '/user'
}


def create_url(key):
    return endpoints['base'] + key


def get_endpoint(key):
    return create_url(endpoints[key])