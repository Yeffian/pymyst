from pymyst import client


class Time:
    def __init__(self):
        pass

    @classmethod
    def expires_in_to_unix_time(cls, created_at, expires_in):
        response = client.get(
            f'https://paste.myst.rs/api/v2/time/expiresInToUnixTime?createdAt={created_at}&expiresIn={expires_in}')

        return response.json()['result']
