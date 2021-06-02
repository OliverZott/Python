"""
Magic Methods:

source:     https://www.pythonforbeginners.com/basics/__str__-vs-__repr
            https://realpython.com/python-f-strings/#option-1-formatting


-   __repr__            --> compute the “official” string representation of an object.
                        https://docs.python.org/3/reference/datamodel.html?highlight=__repr__#object.__repr__

-   __str__             --> compute the “informal” or nicely printable string representation of an object.
                            The return value must be a string object.
                        https://docs.python.org/3/reference/datamodel.html?highlight=__str__#object.__str__

-   __doc__             --> see Docstring_and_Annotations.py

-   __annotations__     --> see Docstring_and_Annotations.py



Author:     Oliver Zott
Date:       24.07.2019
"""


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):     #
        return f'Pizzza with:{self.ingredients}'

    def __str__(self):
        return f'Pizzza({self.ingredients})'


# ========================================================================================================
# Testing:

x = 14
y = "Test String"
print(repr(x))
print(repr(y))
print(str(x))
print(str(y))
print()

nr1 = Pizza(["tomato", "cheese"])
print(">>print(nr1)")
print(nr1)                  # will call __str__ by default --> change with !r flag to __repr__
# print(f"{nr1!r}")
print(">>print(str(nr1))")
print(str(nr1))
print(">>print(repr(nr1))")
print(repr(nr1))
