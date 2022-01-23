import json
import os
from os import path
from pymyst import token

from pymyst.types.Paste import Paste


def test_get_from_id():
    paste = Paste.get_from_id('nss2i2u6')

    other_paste = Paste.get_from_id('23tql1g1', token.API_TOKEN)

    data = paste.data

    other_data = other_paste.data

    assert isinstance(data, dict)
    assert isinstance(data['_id'], str)
    assert isinstance(data['ownerId'], str)
    assert isinstance(data['title'], str)
    assert isinstance(data['createdAt'], int)
    assert isinstance(data['expiresIn'], str)
    assert isinstance(data['deletesAt'], int)
    assert isinstance(data['stars'], int)
    assert isinstance(data['isPrivate'], bool)
    assert isinstance(data['isPublic'], bool)
    assert isinstance(data['tags'], list)
    assert isinstance(data['pasties'], list)
    assert isinstance(data['edits'], list)

    assert isinstance(other_data, dict)
    assert isinstance(other_data['_id'], str)
    assert isinstance(other_data['ownerId'], str)
    assert isinstance(other_data['title'], str)
    assert isinstance(other_data['createdAt'], int)
    assert isinstance(other_data['expiresIn'], str)
    assert isinstance(other_data['deletesAt'], int)
    assert isinstance(other_data['stars'], int)
    assert isinstance(other_data['isPrivate'], bool)
    assert isinstance(other_data['isPublic'], bool)
    assert isinstance(other_data['tags'], list)
    assert isinstance(other_data['pasties'], list)
    assert isinstance(other_data['edits'], list)
