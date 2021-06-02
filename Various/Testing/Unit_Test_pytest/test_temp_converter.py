from Unit_Test_pytest.temp_converter import f2c

import pytest


def test_f2c():
    tf = 212
    expected = 100
    result = f2c(tf)

    assert result == expected
    assert f2c(9941) == 5505
    assert f2c(212) == 100
    assert f2c(32) == 0


# test for interface of function (conform with documentation?)
def test_f2c_type():
    tf = 123.2    # error if int
    result = f2c(tf)
    assert type(result) == type(tf)


# testing function behaviour (exceptions raised?)
def test_f2c_exceptions():
    with pytest.raises(ValueError, match='Input temperature below '):
        f2c(-2523)
