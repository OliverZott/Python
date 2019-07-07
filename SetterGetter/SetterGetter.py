"""
Setter and Getter

Oliver Zott
07.07.2019

https://www.python-course.eu/python3_properties.php
"""


class A:
    def __init__(self):
        self._X = 100

    def getX(self):
        return self._X

    def setX(self, wert):
        if wert < 0:
            return
        self._X = wert

class B:
    def __init__(self):
        self._X = 110

    def getX(self):
        print("call getter")
        return self._X

    def setX(self, wert):
        print("call setter")
        if wert < 0:
            return
        self._X = wert

    X = property(getX, setX)


# -----------------------------------------------------------------------------
print("Setter & Getter:")
a = A()
print(a.getX())

a.setX(300)
print(a.getX())

a.setX(-200)
print(a.getX())
print()

# -----------------------------------------------------------------------------
print("Property-Attribute:")
a._X = 1245
print(a._X)

a._X = -321
print(a._X)

b = B()

b.X = -214
print(b.X)

b.X = 215
