from pymyst.types.User import User

def test_get_response():
    user = User('codemyst')
    response = user.data

    assert isinstance(response, dict)
    assert response['username'] == 'CodeMyst'
    assert response['contributor'] == True
    assert response['_id'] == 'bcfu7961'
    assert response['avatarUrl'] ==  'https://avatars3.githubusercontent.com/u/7966628?v=4'
    assert response['publicProfile'] == True
    assert response['defaultLang'] == 'D'
    assert response['supporterLength'] == 0
