from pymyst import client

class Language:
    def __init__(self, data=None):
        self.data = data

    @classmethod
    def get_from_name(cls, name):
        response = client.get(f'https://paste.myst.rs/api/v2/data/language?name={name}')

        return cls(response.json())

    @classmethod
    def get_from_extension(cls, ext):
        response = client.get(f'https://paste.myst.rs/api/v2/data/languageExt?extension={ext}')

        return cls(response.json())