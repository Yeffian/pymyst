import json

from pymyst import client
from pymyst.exceptions.PasteNotCreated import PasteNotCreatedException
from pymyst.exceptions.PasteNotFound import PasteNotFoundException
from pymyst.exceptions.PasteNotDeleted import PasteNotDeletedException
from pymyst.exceptions.PasteNotEdited import PasteNotEditedException


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
            raise PasteNotCreatedException(f'could not create paste successfully. error {response.reason}')

        return cls(response.json())

    @classmethod
    def delete_paste(cls, paste_id, token=None):
        response = client.delete(f'https://paste.myst.rs/api/v2/paste/{paste_id}', token)

        if response.status_code != 200:
            raise PasteNotDeletedException(f'could not delete paste successfully. error {response.reason}')

    @classmethod
    def edit_paste(cls, paste_id, edit, token=None):
        payload = edit.to_json()
        response = client.patch(f'https://paste.myst.rs/api/v2/paste/{paste_id}', json.dumps(payload), token)

        print(payload)
        print(response.status_code)
        print(f'https://paste.myst.rs/api/v2/paste/{paste_id}')

        if response.status_code != 200:
            raise PasteNotEditedException(f'could not edit paste successfully. error {response.reason}')
