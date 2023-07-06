from __future__ import annotations

from typing import Callable
from typing import List
from typing import Optional
from typing import Union


def print_list(values: List[int]) -> None:
    print(values)


# [..., None]  ..input parameters doesnt matter, output is None
def function(values: List[int], print_fn: Callable[..., None]) -> None:
    print_fn(values)


# Optional[X] means X or None
def append_values(value: int, my_list: Optional[List[int]] = None) -> List[int]:
    if my_list:
        my_list.append(value)
    else:
        my_list = [value]
    return my_list


if __name__ == "__main__":
    lst = [1, 2, 3]
    val = 4

    function(lst, print_list)

    lst2 = append_values(val, lst)
    print(lst2)
