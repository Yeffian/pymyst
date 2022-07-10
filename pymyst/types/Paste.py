import json

from pymyst import client
from pymyst.exceptions.PasteNotCreated import PasteNotCreatedException
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

    @classmethod
    def create_paste(cls, create_paste_info, token=None):
        if not create_paste_info.pasties:
            raise TypeError("Pasties required to make new paste.")
        pasties_json = []

        for pasty in create_paste_info.pasties:
            pasties_json.append(pasty.to_json())

        payload = {
            'title': create_paste_info.title,
            'expiresIn': create_paste_info.expires_in,
            'isPrivate': create_paste_info.is_private,
            'isPublic': create_paste_info.is_public,
            'tags': ','.join(create_paste_info.tags),
            'pasties': pasties_json
        }

        response = client.post(json.dumps(payload), 'https://paste.myst.rs/api/v2/paste/', token)

        if response.status_code != 200:
            raise PasteNotCreatedException(f'could not create paste sucessfully. error {response.reason}')

        return cls(response.json())
