"""
Example 20.1 - Packages

source: https://fabienmaussion.info/scientific_programming/html/20-Package-structure.html

exercise: run script from console or ipython shell!
        $python3  Chapter20_Packages/mymodule.py

Author: Oliver Zott
"""

import numpy as np


pi = 3.14


print('Module top level 1 \n')


def circle_area(radius: float) -> float:
    """ A neat function

    Argument
    --------
        radius : float
            radius of circle

    Return
    ------
        area of the circle : float

    """
    print('in function', circle_area.__name__)
    return pi * radius


def print_n():
    print('The number N in the function is: {}'.format(N))


N = 10


print('Module top level 2 \n')


if __name__ == "__main__":

    print('In main script (mymodule.py): \n')
    print('Circle Area: ', circle_area(3), "\n")

    print(print_n())


