"""
Run in terminal: 
    change to folder and run in terminal (pytest also runs std lib unittest files)
    - $ pytest 

Run in vs code:
    open Unittesting folder directly in vs code:
    - Ctrl + Shift + P
    - select pytest
    - select tests folder
    - run in "Testing" on left hand side

"""

from typing import Any
import pytest
from fastvector import Vector2D

V1 = Vector2D(0, 0)
V2 = Vector2D(-1, 1)
V3 = Vector2D(1.5, -2.5)


@pytest.mark.parametrize(
    ("lhs", "rhs", "exp_res"),
    (
        (V1, V2, Vector2D(-1, 1)),
        (V1, V3, Vector2D(1.5, -2.5)),
        (V3, V2, Vector2D(0.5, -1.5)),
    ),
)
def test_add(lhs: Vector2D, rhs: Vector2D, exp_res: Vector2D) -> None:
    assert lhs + rhs == exp_res


@pytest.mark.parametrize(
    ("lhs", "rhs", "exp_res"),
    (
        (V1, V2, Vector2D(1, -1)),
        (V1, V3, Vector2D(-1.5, 2.5)),
        (V3, V2, Vector2D(2.5, -3.5)),
    ),
)
def test_add(lhs: Vector2D, rhs: Vector2D, exp_res: Vector2D) -> None:
    assert lhs - rhs == exp_res


@pytest.mark.skip(reason="not implemented")
def test_scalar_mult() -> None:
    pass


@pytest.mark.parametrize(
    ("x", "y"),
    (
        (-1, None),
        (None, 5),
        (None, "sdf"),
        # (1, 2),
    ),
)
def test_rasies(x: Any, y: Any) -> None:
    with pytest.raises(TypeError):
        _ = Vector2D(x, y)


def test_repr(capture_stdout: dict) -> None:
    print(repr(Vector2D(1.0, 2.0)))
    assert capture_stdout["stdout"] == "vector.Vector2D(1.0,2.0)\n"


def test_str(capture_stdout: dict) -> None:
    print(str(Vector2D(1.0, 2.0)))
    assert capture_stdout["stdout"] == "str: (1.0, 2.0)\n"
