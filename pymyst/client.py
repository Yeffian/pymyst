import requests


def get(endpoint: str, auth: str = None) -> str:
    headers = {}

    if auth is not None:
        headers = {'Authorization': auth}

    return requests.get(endpoint, headers=headers).text


def post():
    pass
    # TODO: Add post requests


def delete():
    pass
    # TODO: Add delete requests


def patch():
    pass
    # TODO: Add patch requests
