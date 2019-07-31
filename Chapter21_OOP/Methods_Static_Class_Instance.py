"""
Instance, class and static methods!

source: https://realpython.com/instance-class-and-static-methods-demystified/

-   Using staticmethod(function) is considered un-Pythonic way of creating a static function.
    So, in newer versions of Python, you can use the Python decorator @staticmethod.

-   This type of method takes neither a self nor a cls parameter
    (but of course it’s free to accept an arbitrary number of other parameters).
    Therefore a static method can neither modify object state nor class state.
    Static methods are restricted in what data they can access - and they’re
    primarily a way to namespace your methods.

Author:     Oliver Zott
Date:       24.07.2019
"""


class MyClass(object):

    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


# ========================================================================================================
# Examples

m1 = MyClass()
print(m1.method())
print(m1.classmethod())
print(m1.staticmethod())
