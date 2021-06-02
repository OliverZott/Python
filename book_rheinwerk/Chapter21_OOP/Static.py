"""
Static Methods

Oliver Zott
07.07.2019
"""


def m():
    print("Static method")


class A:
    X = 'A-class attribute'  # Class Attribute

    def j(self):
        print("Method j")

    k = staticmethod(m)  # not bound to instance of class, so no 'self' needed

    def n(cls):
        print("Class method n", cls)

    n = classmethod(n)


A.k()  # can be called without creating instance first

# A.l()
a = A()
a.j()

print()
print("Call class attribute: ", A.X)
print("Call class attribute: ", a.X)

print()
A.n()
a.n()
