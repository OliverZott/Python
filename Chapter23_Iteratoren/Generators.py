"""
Chapter 23 - Iterators: Generators

- Generator: want to iterate without creating a list with int (like range)
- "list" or "for-print-loop" NEEDED, TO SHOW ELEMENTS from generator --> Cause they are NOT STORED!!!
- Generator Expressions:

Author: Oliver Zott
Date: 20.09.2019
Update: -
"""


# ------------------------------------------------------------------
# Example 1:
def square_generator(n):
    i = 1
    while i <= n:
        yield i * i
        yield i - 2 * i
        i += 1


# ------------------------------------------------------------------
# Example 2:
def numbers(trigger=False):
    yield "one"
    yield "two"
    if trigger:
        return
    yield "three"
    yield "four"


# ------------------------------------------------------------------
# Example 3: Sub-Generators (page 408)
def guys():
    yield "olli"
    yield "horst"
    return 2  # return value for delegating generator


def girls():
    yield "leni"
    yield "judith"
    return 2  # return value for delegating generator


def names(trigger=True):
    cnt_girls = yield from girls()
    print("{} girls: ".format(cnt_girls))
    if trigger:
        cnt_guys = yield from guys()
        print("{} guys: ".format(cnt_guys))


# ------------------------------------------------------------------
# Example 4: Generator-Expressions (page 413)
print()
print("Example 4:")
print(sum((i*i for i in range(1, 11))))


# ------------------------------------------------------------------
# TEST:

print()
print("Example 1:")
print(list(square_generator(15)))
'''
v = []
for j in square_generator(11):
    # print(j)
    # print(j, end="\n")
    print(j, end="; ")
    v.append(j)
print(v)
'''

print()
print("Example 2:")
print(list(numbers()))
print(list(numbers(True)))

print()
print("Example 3: Sub-Generators")
print(list(names()))
print()
print(list(names(False)))
