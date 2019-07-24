"""
1) Annotations for typecasting in python!

- call with __annotations__

https://docs.python.org/3/library/typing.html
https://www.youtube.com/watch?v=51gwyP5PWM4
- Checking Type-Errors from Annotations with (pip install mypy)
https://www.geeksforgeeks.org/function-annotations-python/

2) Docstring

- call with __doc__


Author:     Oliver Zott
Date:       24.07.2019
"""

import math


class Point:
    """
    Explanation: Instance Represents a point.
    """

    def __init__(self):
        """
        Initialize the point
        """
        self.x = 0
        self.y = 0

    def move(self, val1: int, val2: int):
        """
        move point to new location
        """
        self.x = val1
        self.y = val2

    @property
    def radius(self) -> float:
        """
        calculate radius for given point
        """
        dist = math.sqrt(self.x**2 + self.y**2)
        return dist     # print("Distance from origin of coordinates:", dist)

    @property
    def ptuple(self) -> tuple:
        # return tuple([self.x, self.y])      # create tuple from list
        return self.x, self.y

    @ptuple.setter
    def ptuple(self, tuppel):
        if tuppel[0] < 0:
            self.x = 42
        else:
            self.x = tuppel[0]
        if tuppel[1] < 0:
            self.y = 72
        else:
            self.y = tuppel[1]

    def show(self):
        print("x = {}, y = {}".format(self.x, self.y))


# ------------------------------------------------------
# testing

# help(Point)
print(">>print(Point.__doc__)")
print(Point.__doc__)
print()

print(">>print(Point.move.__annotations__)")
print(Point.move.__annotations__)
print()

p = Point()
p.show()
print(p.radius)

p.x = 125
p.y = -23
p.show()
print(p.radius)
print()

# try setter
p.ptuple = (38, 39)
p.show()
print()

p2 = Point()
p2.ptuple = (-23, 55)
print(">>p2.show()")
p2.show()
print("type of p2: ", type(p2))
print(">>print(p2.ptuple):")
print(p2.ptuple)
print("type of ptuple: ", type(p2.ptuple))
