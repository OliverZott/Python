"""
Singleton - Example1: Naive Singleton

source:
https://refactoring.guru/design-patterns/singleton
https://refactoring.guru/design-patterns/singleton/python/example#lang-features


-   easy to implement a sloppy Singleton; just need to hide constructor and implement a static creation method
-   The same class behaves incorrectly in a multi-threaded environment!
    Multiple threads can call the creation method simultaneously and get several instances of Singleton class.
-   META-CLASSES:
    https://www.python-course.eu/python3_metaclasses.php

Author: Oliver Zott
Version: 1.0 / 14.09.2019
"""


from __future__ import annotations  # needed for line 31 !!
from typing import Optional


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include:
    - base class
    - decorator
    - metaclass
    We will use the metaclass because it is best suited for this purpose.
    """

    _instance: Optional[Singleton] = None
    '''
    - Annotation: blabla: str = "hallo"
    - "_.." intended for internal use
    - “Hey, this isn’t really meant to be a part of the public interface of this class. Best to leave it alone.”
    '''

    def __call__(cls) -> Singleton:
        """
        call is to make instance of class callable (instance as a function!)
        """
        if cls._instance is None:
            cls._instance = super().__call__()
        return cls._instance


class Singleton(metaclass=SingletonMeta):

    def some_business_logic(self):
        print("BlaBla some function")
        """
        Finally, any singleton should define some logic, which can be
        executed on this instance!
        """


if __name__ == "__main__":
    # Client Code

    s1 = Singleton()
    s2 = Singleton()

    print("Check if both created Singleton Instances are the same:")
    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed")

    print()
    print(s1)
    # print(s1())
