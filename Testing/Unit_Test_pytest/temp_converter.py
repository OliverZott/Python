"""
Unit test example with pytest

author: Oliver Zott
"""


def f2c(tf: float) -> float:
    """ Convert degree Fahrenheit to Celsius """
    r = (tf - 32) * 5/9

    # check for physically reasonable results
    # assert r > -273.15
    if r < -273.15:
        raise ValueError('Input temperature below absolute zero!')
    return r  # int(r)


if __name__ == "__main__":
    print(f2c(234))
    print(f2c(32))
