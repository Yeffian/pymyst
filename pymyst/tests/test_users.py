import requests

def test_get_user():
    user = User('codemyst')
    response = user.data()

    assert isinstance(response, dict)
    assert user.name == 'CodeMyst'
    assert user.id == 'bcfu7961'
    assert user.lang == 'D'
    assert user.is_contributer == True
    assert user.avatar_url ==  'https://avatars3.githubusercontent.com/u/7966628?v=4'
    assert user.is_public_profile == True

