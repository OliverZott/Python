
from ptest import metutils


def test_f2c():
    assert metutils.f2c(9941) == 5505
    assert metutils.f2c(212) == 100
    assert metutils.f2c(32) == 0

