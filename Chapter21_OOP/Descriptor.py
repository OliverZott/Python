"""
--- Descriptor Example ---

- object attribute with “binding behavior”
- attribute access has been overridden by methods:  __get__(), __set__(), and __delete__()


source:     https://docs.python.org/3/howto/descriptor.html

Author:     Oliver Zott
Date:       23.07.2019
"""


class RevealAccess(object):     # in Python (from version 3.x), object is root of all classes!!
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print("Retrieving: ", self.name)
        return self.val

    def __set__(self, obj, val):
        print("Updating: ", self.name)
        return self.val


class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5


# ====================================================================
print("---------- To call instance from class MyClass: ----------")
m = MyClass()
print(">> print(m): ")
print(m)

print(">> print(m.x): ")
print(m.x)

print(">> print(m.y): ")
print(m.y)

print(">> m.x = 15: ")
m.x = 15
print(">> print(m.x): ")
print(m.x)

print()
print("---------- To call instance from class RevealAccess directly: ----------")   # NOT POSSIBLE!!!
n = RevealAccess()
print(">> print(n.val): ")
print(n.val)

print(">> n.val = 12345: ")
n.val = 12345

print(">> print(n.val): ")
print(n.val)
