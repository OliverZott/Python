"""
Instance, class and static methods!

source: https://realpython.com/instance-class-and-static-methods-demystified/

-   Using staticmethod(function) is considered un-Pythonic way of creating a static function.
    So, in newer versions of Python, you can use the Python decorator @staticmethod.

-   class methods as factory-functions! (design pattern)

-   Because static method is completely independent from the rest of the class it’s much easier to test.

- 	When make method static? 

Author:     Oliver Zott
Date:       24.07.2019
"""

import math


class MyClass(object):

    def method(self):       # instance method
        """
        - self points to an instance of class when the method is called
        - can access attributes and other methods on the same object (through the self parameter)
        - can also modify class state (access to class through  self.__class__ attribute)
        """
        return 'instance method called', self

    @classmethod
    def classmethod(cls):       # class method
        """
        - cls points to class itself, not to object instance
        - only has access to  cls argument -> it can’t modify object instance state (would require access to self)
        - class methods can still modify class state that applies across all instances of the class
        """
        return 'class method called', cls

    @staticmethod
    def staticmethod():     # static method
        """
        - neither self nor cls (but arbitrary other arguments)
        - CANT modify object state or class state as they are not bound to it
        - restricted in what data they can access - and they’re primarily a way to namespace your methods.
		- Static methods have a very clear use-case. When we need some functionality not w.r.t an Object but 
			w.r.t the complete class, we make a method static.
		- Very dvantageous when we need to create Utility methods as they aren’t tied to an object lifecycle usually
        """
        return 'static method called'


class Pizza:
    def __init__(self, radius, ingredients):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):     #
        return (f'Pizzzzza: {self.ingredients}, '
                f'Radius: {self.radius}cm')

    @property
    def area(self):
        return self.circlearea(self.radius)

    @staticmethod
    def circlearea(r):
        return r**2*math.pi

    @classmethod
    def margherita(cls):
        return cls(35, ['mozzarella', 'tomatoes'])      # cls used to call class and thus __repr__

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


# ========================================================================================================
# General
"""
print( "======================== General ======================== ")
m1 = MyClass()
# Call methods with instance
print(m1.method())
print(MyClass.method(m1))   # alternative call of self-argument of instance method
print(m1.__class__)     # check class to which m1 belongs
print()

print(m1.classmethod())
print(type(m1.classmethod()))
print()

print(m1.staticmethod())
print()

# Call methods on class itself
print("Call methods on class itself: ")
print(MyClass.classmethod())    # Python automatically passes the class itself as first argument
print(MyClass.staticmethod())
# print(MyClass.method())
print()
"""

# ========================================================================================================
# Example: Pizza-class
print("======================== Example: Pizza-class ======================== ")

nr1 = Pizza(14, ["tomato", "cheese"])
print(f"{nr1!r}")       # flag to call __repr__ / though unnecessary here
print()

print(Pizza.margherita())   # use factory function instead calling constructor

p = Pizza(6, ["fish", "chips"])
print(p.area)
print(Pizza.circlearea(6))
