"""
ABC: Example 3

source: https://www.geeksforgeeks.org/abstract-classes-in-python/

-   blueprint for other classes, allowing you to create a set of methods that must be
    created within any child classes
-   Abstract classes allow you to provide default functionality for the subclasses
-   Compared to interfaces abstract classes can have an implementation
-   By defining an abstract base class, you can define a common Application
    Program Interface(API) for a set of subclasses

Author: Oliver Zott
Date: 26.09.2019
"""

import abc
from abc import abstractmethod, ABC


class Polygon(ABC):

    @abstractmethod
    def sides(self):
        pass

    @abstractmethod
    def comment(self):
        print("Abstract Base Class - abstract method called")

    # Abstract Classes can contain concrete and abstract methods
    def concrete_method(self):
        pass


class Triangle(Polygon):

    # overriding abstract methods
    def sides(self):
        print("3 Sides")

    def comment(self):
        super().comment()
        print("Also called by following child-class: '{}'".format(self.__class__.__name__))


class Pentagon(Polygon):

    def sides(self):
        print("5 Sides")

    def comment(self):
        pass


class Hexagon(Polygon):

    def sides(self):
        print("6 Sides")

    def comment(self):
        pass


# ------------ Test -------------

if __name__ == "__main__":

    tri = Triangle()
    tri.sides()
    hex = Hexagon()
    hex.sides()
    print(isinstance(tri, Polygon))
    print(issubclass(Triangle, Polygon))
    print()
    tri.comment()
    # pol = Polygon()  # Can't instantiate abstract base class directly!
