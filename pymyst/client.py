import requests


def get(endpoint: str, auth: str = None):
    headers = {}

    if auth is not None:
        headers['Authorization'] = auth

    return requests.get(endpoint, headers=headers).json()


def post(data: str, endpoint: str, auth: str = None, content_type: str = 'application/json'):
    headers = {'Content-Type': content_type}

    if auth is not None:
        headers['Authorization'] = auth

    return requests.post(endpoint, data=data, headers=headers).json()


def delete():
    pass
    # TODO: Add delete requests


def patch():
    pass
    # TODO: Add patch requests
