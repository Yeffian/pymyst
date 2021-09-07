import requests


class User:
    def __init__(self, data=None):
        self.data = data

    @classmethod
    def get_from_username(cls, username: str):
        response = requests.get(f'https://paste.myst.rs/api/v2/user/{username}')

        return cls(response.json())

    @classmethod
    def user_exist(cls, username: str) -> bool:
        response = requests.get(f'https://paste.myst.rs/api/v2/user/{username}/exists')

        if response.status_code == 200:
            return True
        else:
            return False

