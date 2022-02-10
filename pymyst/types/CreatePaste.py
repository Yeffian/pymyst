class ExpiresIn:
    ONE_HOUR = '1h'
    TWO_HOURS = '2h'
    TEN_HOURS = '10h'
    ONE_DAY = '1d'
    TWO_DAYS = '2d'
    ONE_WEEK = '1w'
    ONE_MONTH = '1m'
    ONE_YEAR = '1y'
    NEVER = 'never'

class CreatePaste:
    def __init__(self, title='untitled', pasties=None, tags=None, expires_in=ExpiresIn.NEVER, is_public=True, is_private=False):

        self.title = title
        self.pasties = pasties
        self.tags = tags
        self.expires_in = expires_in
        self.is_public = is_public
        self.is_private = is_private