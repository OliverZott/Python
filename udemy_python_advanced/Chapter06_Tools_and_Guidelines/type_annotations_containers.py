from __future__ import annotations

from typing import Collection
from typing import Container
from typing import Iterable
from typing import MutableSequence
from typing import Protocol
from typing import Sequence
from typing import Sized


# protocol is used to define structural classes for static type-checking
class SizedIterable(Protocol):
    def __len__(self):
        pass

    def __getitem__(self, idx):
        pass


# def iterate_over_length(obj: Sized) -> None:
# def iterate_over_length(obj: Sequence) -> None:
def iterate_over_length(obj: SizedIterable) -> None:
    """
    pre-requisites:
        obj must implement __len__ and __getitem__
    """
    for i in range(len(obj)):
        print(obj[i])


if __name__ == "__main__":
    values = [1, 2, 3]

    iterate_over_length(values)
