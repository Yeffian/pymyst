from pymyst.types.User import User


def test_get_from_name() -> None:
    response = User.get_from_name('CodeMyst')

    assert isinstance(response, dict)
    assert response['username'] == 'CodeMyst'
    assert response['contributor'] == True
    assert response['_id'] == 'bcfu7961'
    assert response['avatarUrl'] == 'https://avatars3.githubusercontent.com/u/7966628?v=4'
    assert response['publicProfile'] == True
    assert response['defaultLang'] == 'D'
    assert response['supporterLength'] == 0


def test_user_exists() -> None:
    response_first = User.user_exist('YeffyCodeGit')
    response_second = User.user_exist('uwhuihf')

    assert response_first == True
    assert response_second == False
