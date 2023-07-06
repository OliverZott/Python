"""
Custom vector 2D for math operations example

https://docs.python.org/3/library/typing.html
"""

# to use oqn class as type annotation
from __future__ import annotations

import numbers
from functools import total_ordering
from math import sqrt
from typing import SupportsFloat, Union


@total_ordering
class Vector2D:
    """
    Vector2D class for simple vector operations
    """

    def __init__(self, x: SupportsFloat = 0.0, y: SupportsFloat = 0.0) -> None:
        """This is my summary

        Parameters
        ----------
        x : float, optional
            x value, by default 0.0
        y : float, optional
            y value, by default 0.0

        Raises
        ------
        TypeError
            Is raised if wrong input
        """
        if isinstance(x, (int, float)) and isinstance(y, numbers.Real):
            self.x = x
            self.y = y
        else:
            raise TypeError(f"Wrong value for x ({type(x)}) or y ({type(y)})")

    def __call__(self) -> None:
        print(f"Calling __call__ method of {__name__}")

    def __repr__(self) -> str:
        return f"vector.Vector2D({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"str: ({self.x}, {self.y})"

    def __abs__(self) -> float:
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __eq__(self, other_vector: object) -> bool:
        if not isinstance(other_vector, Vector2D):
            return False
        return self.x == other_vector.x and self.y == other_vector.y

    def __lt__(self, other_vector: Vector2D) -> bool:
        # call dunder method or inbuild
        return self.__abs__() < abs(other_vector)

    def __add__(self, other_vector: Vector2D) -> Vector2D:
        if not isinstance(other_vector, Vector2D):
            raise TypeError("You must pass in a Vector2D instance!")
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector2D(x, y)

    def __sub__(self, other_vector: Vector2D) -> Vector2D:
        if not isinstance(other_vector, Vector2D):
            raise TypeError("You must pass in a Vector2D instance!")
        x = self.x - other_vector.x
        y = self.y - other_vector.y
        return Vector2D(x, y)

    def __mul__(self, other: Union[Vector2D, SupportsFloat]) -> Vector2D:
        """Skalarproduct or componentwise multiplication

        Parameters
        ----------
        other : Union[Vector2D, SupportsFloat]
            scalar or vector

        Returns
        -------
        Vector2D
            Result of multiplication (componentwise or scalar)

        Raises
        ------
        TypeError
            If wrong input type, throws error
        """
        if isinstance(other, Vector2D):
            x = self.y * other.x - self.x * other.y
            y = self.x * other.y - self.y * other.x
            return Vector2D(x, y)
        elif isinstance(other, (int or float)):
            self.x *= other
            self.y *= other
            return self
        else:
            raise TypeError("Pass int/float or a Vector2D")

    def __truediv__(self, other: float):
        return Vector2D(self.x / other, self.y / other)


def main():
    v1 = Vector2D(2.3, 6)
    res = v1 / "df"
    res2 = v1 / 2
    res3 = v1 / 2.5
