import requests


def get(endpoint: str, auth: str = None) -> str:
    headers = {}

    if auth is not None:
        headers = {'Authorization': auth}

    return requests.get(endpoint, headers=headers).text


def post(endpoint: str, auth: str, content_type: str='application/json') -> str:
    headers = {'Content-Type': content_type}

    if auth is not None:
        headers['Authorization'] = auth

    return requests.get(endpoint, headers=headers).text

def delete():
    pass
    # TODO: Add delete requests


def patch():
    pass
    # TODO: Add patch requests
