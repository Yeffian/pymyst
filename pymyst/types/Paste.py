from pymyst import client


class Paste:
    def __init__(self, data=None):
        self.data = data

    @classmethod
    def get_from_id(cls, id):
        response = client.get(f'https://paste.myst.rs/api/v2/paste/{id}')

        if response.status_code != 200:
            pass
            # raise PasteNotFoundException()

        return cls(response.json())
    