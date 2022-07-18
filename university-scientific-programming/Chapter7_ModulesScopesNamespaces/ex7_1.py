"""
Variablesc scopes

source: https://fabienmaussion.info/scientific_programming/html/07-Import-Scopes.html

Author: Oliver Zott
Date: 2019-12-03
"""


def foo():
    i = 5
    print(i, 'i in foo()')


i = 17
print(i, 'i global')

k = 3
print(k, 'k global')


def bar():
    print(k, 'k in bar()')


if __name__ == "__main__":
    foo()
    bar()
