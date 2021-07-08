"""
ABC Classes - Example 4

source: https://www.tutorialspoint.com/abstract-base-classes-in-python-abc

-   "abc.ABCMeta"  ...
    https://docs.python.org/3/library/abc.html
    https://stackoverflow.com/questions/33335005/is-there-any-difference-between-using-abc-vs-abcmeta

-   Instead of subclassing from abstract base class, it can be registered as
    abstract base by register class decorator.

Author: Oliver Zott
Date: 29.09.2019
"""


import abc


class Shape(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, x, y):
        self.l = x
        self.b = y

    def area(self):
        return self.l * self.b


# register instead of subclassing:
@Shape.register
class Triangle():

    def __init__(self, x, y):
        self.l = x
        self.b = y

    def area(self):
        return (self.l * self.b) / 2


# ----------------------------------------------
# Example

r1 = Rectangle(7, 3)
print(r1.area())

t1 = Triangle(4, 8)
print(t1.area())
