from pymyst.types.Paste import Paste


def test_get_from_id():
    paste = Paste.get_from_id('nss2i2u6')

    data = paste.data

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
