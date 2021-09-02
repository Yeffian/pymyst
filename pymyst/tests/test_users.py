import requests

def test_get_user():
    # refactor all this....
    response = requests.get('https://paste.myst.rs/api/v2/user/tsujin/exists')

    assert response.status_code == 200
