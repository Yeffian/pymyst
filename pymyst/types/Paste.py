import json

from pymyst import client
from pymyst.exceptions.PasteNotFound import PasteNotFoundException


class Paste:
    def __init__(self, data):
        self.data = data


    @classmethod
    def get_from_id(cls, id, token=None):
        response = client.get(f'https://paste.myst.rs/api/v2/paste/{id}', token)

        if response.status_code != 200:
            raise PasteNotFoundException('Unable to get paste.')

        return cls(response.json())