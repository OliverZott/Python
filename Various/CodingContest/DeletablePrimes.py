"""
Coding Contest: Example 1

- https://catcoder.codingcontest.org/training/1207/play

ToDo:   - No Efficient!!
        - better way then global vars??
        - recursive functions in general?!

- Solutions: https://stackoverflow.com/questions/33505735/recursive-function-for-tracing-deletable-primes-python-3

Author: Oliver Zott
Date: 04.10.2019
"""

import itertools
import math


# ============= SOLUTION =================================================================
def isPrime(x):
    if x <= 1:
        return False
    for i in range(1, int(math.sqrt(x)) + 1):
        if not math.gcd(i, x) == 1:
            # print(i)
            return False
    return True


def is_prime_number(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False
    return True


def isDeletablePrime(n, *, valor=True):
    if isPrime(n):
        N = str(n)
        S = len(N)
        if S > 1 and any(p in N for p in "2 3 5 7".split()):
            resul = list()
            for num in set(map(lambda x: int("".join(x)), itertools.combinations(N, S-1))):
                # set(...) eliminate potential duplicates like with 331 there are 2 way
                # to get 31, removing the first or second 3
                temp = isDeletablePrime(num, valor=True)
                if temp:
                    resul.extend((n,)+tt for tt in temp)
            if valor:
                return tuple(filter(lambda r: len(r) == S, resul))
            else:
                return any(len(r) == S for r in resul)
        elif n in {2, 3, 5, 7}:  # base case
            return ((n,),) if valor else True
    return tuple() if valor else False  # base case and default
# ================================================================================================


def check_prime(value):

    trigger = True

    if value > 1:
        for i in range(2, value):
            # print("i:", i)
            if (value % i) == 0:
                # print("% = 0")
                trigger = False
                break
    else:
            trigger = False

    return trigger


def remove_digit(value, n):
    first_part = value[:n]
    last_part = value[n+1:]
    return first_part + last_part


counter = 0
prime_list = []
tmp = []


def delete_prime(value):

    val = str(value)
    global counter
    global prime_list
    global tmp

    if check_prime(value):
        for i in range(0, len(val)):
            # print("counter: ", counter)
            cut_digit = int(remove_digit(val, i))
            # tmp.append(cut_digit)
            # print("i:", i)
            # print("new digit: ", cut_digit)
            if check_prime(cut_digit):

                # print("prime?: ", check_prime(cut_digit))
                if (len(str(cut_digit))) == 1:
                    prime_list.append(cut_digit)
                    # prime_list.append(tmp)
                    counter += 1
                    # print("list: ", prime_list)
                    # print("counter: ", counter)
                else:
                    delete_prime(cut_digit)
            else:
                # print("not prime!")
                # print()
                continue

    return prime_list, counter


# ------------------------------
# print(is_prime_number(20))
# print(check_prime(1))
# print()

print("4125673: ", delete_prime(2147483059))
# print(4125673, "->", isDeletablePrime(337424981) )
# print(len(isDeletablePrime(46216567629137)))

