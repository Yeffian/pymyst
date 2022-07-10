import json
from pymyst.types.User import User
import os
import pytest
from pymyst import token


def test_get_from_user_token():
    user = User.get_from_user_token(token.API_TOKEN)

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
