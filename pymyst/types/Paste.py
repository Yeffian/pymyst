from pymyst import client
from pymyst.exceptions.PasteNotFound import PasteNotFoundException


class Paste:
    def __init__(self, data=None):
        self.data = data

    @classmethod
    def get_from_id(cls, id):
        response = client.get(f'https://paste.myst.rs/api/v2/paste/{id}')

        if response.status_code != 200:
            raise PasteNotFoundException('Unable to get paste.')

        return cls(response.json())
