
class A:
    def __init__(self):
        print('hello, constructor of class A speaking :)')

    def zeige(self):
        print('class A standard-output speaking now')

class B:
    def __init__(self):
        print('hello, constructor of class B speaking :)')

    def zeige(self):
        print('class B standard output')

# ----------------------------------------------------------------------------------
# child classes:

class A1(A):
    def __init__(self):
        super().__init__()

    def zeige(self):
        print('print of child-class A1')

class A2(A1):
    def __init__(self):
        super().__init__()

    def zeige(self):
        super().zeige()
        print('print of child-child-class A2')

class B1(B):
    def __init__(self):
        super().__init__()


