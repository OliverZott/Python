"""
Setter and Getter
Book page 358

https://docs.python.org/3/howto/descriptor.html#properties
https://www.python-course.eu/python3_properties.php

Idea:           Restrict access to Class-Attributes by specific rules
Alternative:    __get__ __set__  -> Descriptor

Author:     Oliver Zott
Date:   23.07.2019
"""


class A:
    def __init__(self):     # Constructor (magic method) ...called when new instance is created
        self._X = 100       # Class Attribute

    def getX(self):         # Class Method
        return self._X

    def setX(self, value):
        if value < 0:
            return
        self._X = value


class B:
    def __init__(self):
        self._X = 110

    def getx(self):
        print("call getter")
        return self._X

    def setx(self, value):
        print("call setter")
        if value < 0:
            return
        self._X = value
    XY = property(getx, setx)


# -----------------------------------------------------------------------------
print("Setter & Getter:")
a = A()
print(a.getX())
print()

print(a)
print(a._X)     # still can access without getter (but not recommended)
print()

a.setX(300)
print(a.getX())
print()

print("set to -200: ")
a.setX(-200)
print(a.getX())
print()

# -----------------------------------------------------------------------------
print("============================================")
print("Class A without Property-Attribute:")
a._X = 1245
print(a._X)
print()

print("set instance a of class A with 'a._X = -321': ")
a._X = -321
print(a._X)
print("obviously no setter called!")
print()

print("Class B WITH Property-Attribute:")
b = B()
print()

print("Set instance b of class B with 'b.XY = -214 / b.XY = 215': ")
b.XY = -214
print(b.XY)
print()

b.XY = 215
bxy = b.XY
print(bxy)
