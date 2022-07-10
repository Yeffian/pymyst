import requests


def get(endpoint, auth=None):
    headers = {}

    if auth is not None:
        headers['Authorization'] = auth

    return requests.get(endpoint, headers=headers)


def post(data, endpoint, auth=None, content_type='application/json'):
    headers = {'Content-Type': content_type}

    if auth is not None:
        headers['Authorization'] = auth

    return requests.post(endpoint, data=data, headers=headers)


def delete(endpoint, auth):
    # deleting things always requires the authorization header so its not optional
    headers = {'Authorization': auth}

    return requests.delete(endpoint, headers=headers)


def patch():
    
