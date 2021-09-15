import json
from pymyst.types.User import User
import os


def load_config():
    curr_path = os.path.dirname(os.path.abspath(__file__))
    config = os.path.join(curr_path, 'data.json')
    return json.load(open(config))


def test_get_from_user_token():
    config = load_config()
    user = User.get_from_user_token(config['token'])

    response = user.data

    assert isinstance(response, dict)

    assert isinstance(response['username'], str)
    assert isinstance(response['contributor'], bool)
    assert isinstance(response['_id'], str)
    assert isinstance(response['avatarUrl'], str)
    assert isinstance(response['publicProfile'], bool)
    assert isinstance(response['defaultLang'], str)
    assert isinstance(response['supporterLength'], int)
    assert isinstance(response['stars'], list)
    assert isinstance(response['serviceIds'], dict)


def test_get_from_name():
    user = User.get_from_username('CodeMyst')

    response = user.data

    assert isinstance(response, dict)

    assert isinstance(response['username'], str)
    assert isinstance(response['contributor'], bool)
    assert isinstance(response['_id'], str)
    assert isinstance(response['avatarUrl'], str)
    assert isinstance(response['publicProfile'], bool)
    assert isinstance(response['defaultLang'], str)
    assert isinstance(response['supporterLength'], int)


def test_user_exists():
    response_first = User.user_exist('YeffyCodeGit')
    response_second = User.user_exist('uwhuihf')

    assert response_first == True
    assert response_second == False
