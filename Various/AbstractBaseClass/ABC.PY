"""
ABC Classes - Example 1

source: https://www.python-course.eu/python3_abstract_classes.php

- abstract classes: contain abstract methods
- abstract methods: are declared but contain NO IMPLEMENTATION
- abstract classes: may not be instantiated
- abstract classes: require subclasses to provide implementation for abstract methods
- subclasses of abstract class: are not required to implement abstract method of parent class ??????
- subclasses of abstract class: cannot be instantiated unless all of its abstract methods are overridden!

Author: Oliver Zott
Date: 26.09.2019
"""

from abc import ABC, abstractmethod


# ----------------------------------------------
# Example 1:

class AbstractClass:

    def __init__(self):
        print("AbstractClass instantiated")

    def function(self):
        pass


class B(AbstractClass):

    def __init__(self):
        super().__init__()
        print("Child Class B instantiated")

    pass


# Not abstract class because:
# 1. instance can be instantiated
# 2. no implementation of "function" in class definition of B
a = AbstractClass()
print()
b = B()
print()


# ----------------------------------------------
# Example 2:

class AbstractClassExample(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass


class DoAdd42(AbstractClassExample):

    def do_something(self):
        return self.value + 42


class DoMul3(AbstractClassExample):

    #def do_something(self):
        #return self.value * 3
    pass

# Test:
x = DoAdd42(3)
y = DoMul3(4)
print(x)
print("x.do_something(): ", x.do_something())
print("y.do_something(): ", y.do_something())








