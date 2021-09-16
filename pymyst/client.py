import requests


def get(endpoint, auth=None):
    headers = {}

    if auth is not None:
        headers['Authorization'] = auth

    return requests.get(endpoint, headers=headers).json()


def post(data, endpoint, auth, content_type='application/json'):
    headers = { 'Content-Type': content_type }

    if auth is not None:
        headers['Authorization'] = auth

    return requests.post(endpoint, data=data, headers=headers).json()


def delete():
    pass
    # TODO: Add delete requests


def patch():
    pass
    # TODO: Add patch requests
