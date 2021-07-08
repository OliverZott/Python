"""
Coding Contest: Fibonacci

Author: Oliver Zott
Date: 04.10.2019
"""


def fib(n):

    f = 0
    f0 = 0
    f1 = 1

    while n-1 > 0:
        f = f0 + f1
        f0, f1 = f1, f

        n -= 1

    return f


if __name__ == "__main__":
    print(fib(38))
