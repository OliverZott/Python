"""
ABC Classes - Example 2

source: https://www.python-course.eu/python3_abstract_classes.php

- abstract method can have an implementation in the abstract class!
- abstract method can be invoked with super() call mechanism

Author: Oliver Zott
Date: 26.09.2019
"""

from abc import ABC, abstractmethod


class AbstractClass(ABC):

    @abstractmethod
    def do_smth(self):
        print("abstract base-class function")


class Child(AbstractClass):

    def do_smth(self):
        super().do_smth()
        print("some Addition from child class")


if __name__ == "__main__":

    x = Child()
    x.do_smth()
