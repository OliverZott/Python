"""
Python Main: __name__

sources:
- https://www.geeksforgeeks.org/__name__-special-variable-python/
- https://stackoverflow.com/questions/419163/what-does-if-name-main-do

Oliver Zott
21.08.2019
"""

import math


print("File1 __name__ = {}".format(__name__))


def functionA():
    print("function A called")


def functionB():
    print("Function B called: {}".format(math.sqrt(100)))


if __name__ == '__main__':
    print()
    print("File is run directly!")
else:
    print()
    print("File seems to be imported!")
