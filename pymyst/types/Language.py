from pymyst import client
from pymyst.exceptions.LanguageNotFound import LanguageNotFoundException


class Language:
    def __init__(self, data=None):
        self.data = data

    @classmethod
    def get_from_name(cls, name):
        response = client.get(f'https://paste.myst.rs/api/v2/data/language?name={name}')

        if response.status_code != 200:
            raise LanguageNotFoundException('Unable to get language')

        return cls(response.json())

    @classmethod
    def get_from_extension(cls, ext):
        response = client.get(f'https://paste.myst.rs/api/v2/data/languageExt?extension={ext}')

        if response.status_code != 200:
            raise LanguageNotFoundException('Unable to get language')

        return cls(response.json())
