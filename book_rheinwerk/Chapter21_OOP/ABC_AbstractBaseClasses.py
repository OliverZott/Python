"""
ABC - Abstract Base Classes in python

Source:     https://www.python-course.eu/python3_abstract_classes.php
            https://dbader.org/blog/abstract-base-classes-in-python


 -  Abstract classes are classes that contain one or more abstract methods.

 -  An abstract method is a method that is declared, but contains no implementation.

 -  Abstract classes may not be instantiated, and require subclasses to provide
    implementations for the abstract methods.

 -  Subclasses of an abstract class in Python are not required to implement
    abstract methods of the parent class.


Author:     Oliver Zott
Date:       01.08.2019
"""


from abc import ABC, abstractmethod


class AbstractClass:

    def do_something(self):
        pass


class B(AbstractClass):
    pass

# --------------------------------------------------


class AbstractClassExample(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass


class DoAdd42(AbstractClassExample):
    pass


# ========================================================================
# Test Example 1:

a = AbstractClass()
b = B()
print(a)
print(b)

# no abstract class because:
#   - we can instantiate an instance from
#   - we are not required to implement do_something in the class definition of B


# ========================================================================
# Test Example 2:

x = DoAdd42(4)
print(x)        # TypeError: DoAdd42 cant be instantiated because abstract method is not implemented
