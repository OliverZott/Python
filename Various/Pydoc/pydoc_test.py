"""
This is header of pydoc_test.py

Author: Oliver Zott
Date: 20.09.2019
"""
import pydoc


class MyClass:
    """" Meine Klasse

    nur ein test
    blabla
    """
    print("MyClass class... ")

    def my_class_function(self):
        """ Diese Funktion macht nüscht

        blabla
        """
        print("my_class_function.")


def MyFunction():
    """ Nur eine Funktion die nichts macht

    blabla
    """
    pass


if __name__ == "__main__":
    print(MyClass.__doc__)
    print()

    print(MyFunction.__doc__)

    # pydoc -w MyClass

