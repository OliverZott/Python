"""
Oliver Zott
07.07.2019
"""


class A:
    def __init__(self, test):
        self.text = test

    def classplot(self):
        print("class A print: ", self.text)


class B:
    # def __init__(self):

    def classplot(self):
        print("class B print ")


class A1(A):
    def __init__(self, test):
        super().__init__(test)

    def classplot(self):
        super().classplot()
        print("class A1 print")


class A2(A1):

    def classplot(self):
        super().classplot()
        print("class A2 print")


class B2(A2):
    def __init__(self, test):
        super().__init__(test)
        self.text = test
    b = B()

    def classplot(self):
        super().classplot()
        self.b.classplot()


# --------------------------------------------------------------------------------------
print("a = A")
a = A("blabla")
a.classplot()
print()

print("a1 = A1")
a1 = A1("sdf")
a1.classplot()
print()

print("a2 = A2")
a2 = A2("sdf")
a2.classplot()
print()

print("b2 = B2")
b2 = B2("gkkkkr")
b2.classplot()
print()

# --------------------------------------------------------------------------------------
# Class Functions

print(issubclass(A1, A))
print(isinstance(a2, A2))

