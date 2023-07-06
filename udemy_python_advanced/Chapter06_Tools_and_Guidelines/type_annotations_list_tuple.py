from __future__ import annotations

from typing import Any, List, Tuple, Union

MyNumber = Union[int, float]


def append_list(lst: List[MyNumber], val: MyNumber):
    lst.append(val)


def print_3d_tuple(tpl: Tuple[MyNumber, MyNumber, MyNumber]):
    for val in tpl:
        print(val)


if __name__ == "__main__":
    l: List[Union[int, float]] = [1, 2, 3]
    t = (1, 2, 3, 4)

    append_list(l, 5)

    print_3d_tuple(t)
