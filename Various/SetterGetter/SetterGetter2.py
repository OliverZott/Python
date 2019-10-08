"""
Setter / Getter

-

source: https://www.python-course.eu/python3_properties.php

Oliver Zott
Date: 05.10.2019
"""


# ---------------------------------------------------------
# Example1: Java-Style
class P(object):

    def __init__(self, x):
        self.__x = x        # private attribute (java-way)

    def get_x(self):
        return self.__x

    def set_x(self, input):
        if input < 0:
            self.__x = 0
        elif input > 1000:
            self.__x = 1000
        else:
            self.__x = input


# ---------------------------------------------------------
# Example2:
class Q:

    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, input):
        if input < 0:
            self.__x = 0
        elif input > 1000:
            self.__x = 1000
        else:
            self.__x = input


# ---------------------------------------------------------
# Example1: Java-Style
if __name__ == "__main__":

    # Example 2
    q1 = Q(4353634)
    print(q1.x)
    q1.y = 10002
    print(q1.x)
    print(q1.y)
    print()

    # Example 1
    p1 = P(1)
    print(p1.get_x())
    p1.__x = 20         # only with double underline "private"
    print(p1.get_x())
    p1.set_x(20)
    print(p1.get_x())
    print()