endpoints = {
    'base': 'https://paste.myst.rs/api/v2',
    'data': '/data',
    'time': '/time',
    'paste': '/paste',
    'user': '/user'
}


def create_url(key: str):
    return endpoints['base'] + key


def get_endpoint(key: str):
    return create_url(endpoints[key])