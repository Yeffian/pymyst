import requests

class User:
    def __init__(self, username):
        # later this can become something like: client.get_user(username) if we want
        response = requests.get(f'https://paste.myst.rs/api/v2/user/{username}')

        #TODO: DESIGN DECISION- do we want to refactor this so the User object contains these fields?
        self.data = response.json()
