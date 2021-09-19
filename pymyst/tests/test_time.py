from pymyst.types.Time import Time


def test_expires_in_to_unix_time():
    time = Time.expires_in_to_unix_time(1588441258, '1w')

    assert time == 1589046058
