from pymyst.types.Language import Language


def test_get_from_name():
    lang = Language.get_from_name('Python')

    data = lang.data

    assert isinstance(data, dict)
    assert isinstance(data['ext'], list)
    assert isinstance(data['name'], str)
    assert isinstance(data['color'], str)
    assert isinstance(data['file'], str)
    assert isinstance(data['mode'], str)
    assert isinstance(data['mimes'], list)


def test_get_from_extension():
    lang = Language.get_from_extension('py')

    data = lang.data

    assert isinstance(data, dict)
    assert isinstance(data['ext'], list)
    assert isinstance(data['name'], str)
    assert isinstance(data['color'], str)
    assert isinstance(data['file'], str)
    assert isinstance(data['mode'], str)
    assert isinstance(data['mimes'], list)
