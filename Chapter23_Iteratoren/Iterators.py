"""
Chapter 23 - Iterators

- Iterator: abstraction layer; used on arbitrary container
-

Author: Oliver Zott
Date: 24.09.2019
Update: -
"""


# -----------------------------------------------------------------
# Example 1:

class Fibonacci:

    def __init__(self, max_n):
        self.MaxN = max_n
        self.N = 0
        self.A = 0
        self.B = 0
        print("Superclass constructor called!")

    def __iter__(self):
        """
        no-parameter
        returns reference to object itself
        """
        self.N = 0
        self.A = 0
        self.B = 1
        return self

    def __next__(self):
        """
        provides next element in each call
        """
        if self.N < self.MaxN:
            self.N += 1
            self.A, self.B = self.B, self.A + self.B  # Import to put in one line!
            return self.A
        else:
            raise StopIteration


class GoldenRatio(Fibonacci):

    # Not necessary ... inherits automatically!
    def __init__(self, kmax):
        super().__init__(kmax)
        print("Subclass Constructor called!")

    def __next__(self):
        Fibonacci.__next__(self)
        return self.B / self.A


class Fibonacci2:

    def __init__(self, max_n):
        self.MaxN = max_n

    def __iter__(self):
        n = 0
        a, b = 0, 1
        for n in range(self.MaxN):  # while n < self.MaxN: also possible, but need n+1
            a, b = b, a + b
            # n += 1
            yield a


# -----------------------------------------------------------------
# Example 2:

for i in range(10):
    print(i, end=" ")
print()

it = iter(range(3))
print(it)
iter(range(10))
print(next(it))
print(next(it))
print(next(it))
print(next(it, 666))  # Exception is thrown here if no argument


# Own Exception:
def test():
    ite = iter(range(5))
    while True:
        try:
            print(next(ite), end="\n")
        except StopIteration:
            break


test()
print()


# -----------------------------------------------------------------
# Example 3:

def test2():
    yield 10
    yield 20
    return 1337


def test2_call(arg: test2()):
    while True:
        try:
            print(next(arg))
        except StopIteration as e:
            print("Return: ", e.value)
            break


i2 = test2()
test2_call(i2)
print()


# -----------------------------------------------------------------
# Test:

fib = Fibonacci(14)
print(type(fib))
print(list(fib))
print(sum(Fibonacci(60)))
print()

grat = GoldenRatio(20)
print(grat)
print(list(grat))
print()

fib2 = Fibonacci2(14)
print(list(fib2))
