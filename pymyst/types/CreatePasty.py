class CreatePasty:
    def __init__(self, language='Plain Text', title='untitled', code=None):
        if code is None:
            raise TypeError('source code required to construct a pasty')

        self.language = language
        self.code = code
        self.title = title

    def to_json(self):
        return {
            'language': self.language,
            'title': self.title,
            'code': self.code
        }
