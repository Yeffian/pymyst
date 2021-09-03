import requests


class User:
    def __init__(self):
        self.data = None

    @classmethod
    def get_from_name(cls, username: str) -> dict:
        response = requests.get(f'https://paste.myst.rs/api/v2/user/{username}')

        return response.json()

    @classmethod
    def user_exist(cls, username: str) -> bool:
        response = requests.get(f'https://paste.myst.rs/api/v2/user/{username}/exists')

        if response.status_code == 200:
            return True
        else:
            return False

