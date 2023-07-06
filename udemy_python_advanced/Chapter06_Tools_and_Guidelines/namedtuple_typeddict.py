from typing import NamedTuple, TypedDict, Union


# for data (not mutable)
class User(NamedTuple):
    name: str
    age: int = 63


# data in fomr as dict
class Point2D(TypedDict):
    x: int
    y: int
    label: Union[str, int]


def main() -> None:
    user1 = User("olli")
    print(user1)
    print(dir(user1))  # show all implemented dunders

    point_a: Point2D = {"x": 1, "y": 3, "label": "nice"}
    print(point_a)

    point_b: Point2D = {"x": 1, "y": 3, "label": 42}
    print(point_b)


if __name__ == "__main__":
    main()
