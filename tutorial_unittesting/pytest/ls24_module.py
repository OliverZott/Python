"""An example Python module."""

from typing import List


def total(xs: List[float]) -> float:
    """Returns the sum of xs."""
    result: float = 0.0
    for x in xs:
        result += x
    return result


def join(xs: List[float], delimeter: str) -> str:

    if len(xs) == 0:
        return ""

    result: str = ""

    i = 0
    while i < len(xs):
        if i == len(xs)-1:
            result += str(xs[i])
        else:
            result = result + str(xs[i]) + delimeter
        i += 1

    return result


if __name__ == "__main__":

    print(total([1, 2, 3]))
    print(total([]))

    print(join([1, 2, 3.1], "-"))
