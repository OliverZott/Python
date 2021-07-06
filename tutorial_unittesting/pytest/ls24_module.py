"""An example Python module."""

from typing import List


def total(xs: List[float]) -> float:
    """Returns the sum of xs."""

    temp = 0

    for x in xs:
        temp += x

    return temp


if __name__ == "__main__":

    print(total([1, 2, 3]))
    print(total([]))
