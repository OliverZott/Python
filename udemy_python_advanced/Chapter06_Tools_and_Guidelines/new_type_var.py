from __future__ import annotations

from typing import NewType

# create new custom data-type
UserId1 = NewType("UserId1", int)

# type-alias
UserId2 = int


def name_by_id1(user_id: UserId1) -> None:
    print(user_id)


def name_by_id2(user_id: UserId2) -> None:
    print(user_id)


def main() -> None:
    name_by_id1(UserId1(42))  # NewType -> got int
    name_by_id1(UserId2(42))

    name_by_id2(UserId1(42))  # int -> got newtype
    name_by_id2(UserId2(42))


if __name__ == "__main__":
    main()
