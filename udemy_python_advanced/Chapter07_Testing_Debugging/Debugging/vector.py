import numbers
from functools import total_ordering
from math import sqrt


@total_ordering
class Vector2D:
    """
    Vector2D class for simple vector operations
    """

    def __init__(self, x=0.0, y=0.0) -> None:
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

    def __call__(self):
        print(f"Calling __call__ method of {__name__}")

    def __repr__(self):
        return f"vector.Vector2D({self.x}, {self.y})"

    def __str__(self):
        return f"str: ({self.x}, {self.y})"

    def __abs__(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __eq__(self, other_vector):
        return self.x == other_vector.x and self.y == other_vector.y

    def __lt__(self, other_vector):
        # call dunder method or inbuild
        return self.__abs__() < abs(other_vector)

    def __add__(self, other_vector):
        if not isinstance(other_vector, Vector2D):
            raise TypeError("You must pass in a Vector2D instance!")
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector2D(x, y)

    def __sub__(self, other_vector):
        if not isinstance(other_vector, Vector2D):
            raise TypeError("You must pass in a Vector2D instance!")
        x = self.x - other_vector.x
        y = self.y - other_vector.y
        return Vector2D(x, y)

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            x = self.y * other.x - self.x * other.y
            y = self.x * other.y - self.y * other.x
            return Vector2D(x, y)
        elif isinstance(other, (int or float)):
            self.x *= other
            self.y *= other
            return self

    def __truediv__(self, other):
        return Vector2D(self.x / other, self.y / other)


if __name__ == "__main__":
    v1 = Vector2D(2.3, 5.2)
    v2 = Vector2D(1.4, 3.1)

    print(repr(v1))
    print(str(v1))
    print(v1)  # calls __str__

    print(v1 < v2)
    print(v1 > v2)
    print(v1 == v2)
    print(v1 != v2)

    print(v1 * v2)
    print(v1 * 4)

    v3 = Vector2D(2, 1)
    v4 = Vector2D(1, 0)

    print(v3 * v4)
    print(v3 * 3)
    print(v3 / 2)
