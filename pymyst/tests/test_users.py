import json
from pymyst.types.User import User
import os
import pytest


def load_config():
    curr_path = os.path.dirname(os.path.abspath(__file__))
    config = os.path.join(curr_path, 'data.json')
    return json.load(open(config))


def test_get_from_user_token():
    config = load_config()
    user = User.get_from_user_token(config['token'])

    validate_user_data(user.data)

    assert isinstance(user.data['stars'], list)
    assert isinstance(user.data['serviceIds'], dict)


def test_get_from_name():
    user = User.get_from_username('CodeMyst')


    validate_user_data(user.data)


def validate_user_data(data):
    assert isinstance(data, dict)

    assert isinstance(data['username'], str)
    assert isinstance(data['contributor'], bool)
    assert isinstance(data['_id'], str)
    assert isinstance(data['avatarUrl'], str)
    assert isinstance(data['publicProfile'], bool)
    assert isinstance(data['defaultLang'], str)
    assert isinstance(data['supporterLength'], int)


def test_user_exists():
    response_first = User.user_exist('YeffyCodeGit')
    response_second = User.user_exist('uwhuihf')

    assert response_first == True
    assert response_second == False
