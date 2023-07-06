from __future__ import annotations

from typing import Dict
from typing import Mapping
from typing import Union


def iterate_over_dict(my_dict: Dict[str, Union[int, float]]) -> Mapping[str, Union[int, float]]:
    for key, val in my_dict:
        print(f"key: {key} - val: {val}")
    return my_dict


# since python 3.10
def iterate_over_dict2(my_dict: dict[str, int | float]) -> dict[str, int | float]:
    for key, val in my_dict:
        print(f"key: {key} - val: {val}")
    return my_dict


if __name__ == "__main__":
    keys = ["key1", "key2"]
    values = [2, 3.3]
    my_dict: Dict[str, Union[int, float]] = zip(keys, values)

    iterate_over_dict(my_dict)
