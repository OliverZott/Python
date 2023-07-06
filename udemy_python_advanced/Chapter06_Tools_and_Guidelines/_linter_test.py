"""
Linters


Flake 8 - https://flake8.pycqa.org/en/latest/
    flake8 .\test.py

Pylint - https://pylint.readthedocs.io/en/stable/
    pylint .\test.py
    pylint --generate-rcfile > .pylintrc
"""
import math

q = [1, 2, 3]  # comment


def print_stuff(l):  # noqa: E741
    print(l)


def gen():
    # list1 = list(x for x in range(5))
    list1 = list(range(5))
    return list1
