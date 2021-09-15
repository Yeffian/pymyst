from pymyst import client
import requests


class User:
    def __init__(self, data=None):
        self.data = data

    @classmethod
    def get_from_username(cls, username):
        response = client.get(f'https://paste.myst.rs/api/v2/user/{username}')

        return cls(response)

    @classmethod
    def user_exist(cls, username):
        response = requests.get(f'https://paste.myst.rs/api/v2/user/{username}/exists')

        if response.status_code == 200:
            return True
        else:
            return False

    @classmethod
    def get_from_user_token(cls, token):
        response = client.get(f'https://paste.myst.rs/api/v2/user/self', token)

        return cls(response)
