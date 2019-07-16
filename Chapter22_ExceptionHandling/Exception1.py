"""
Exception Handling Example 1

page ...

Oliver Zott
13.07.2019

Shadowing: https://stackoverflow.com/questions/19902127/what-is-the-pythonic-way-to-avoid-shadowing-variables
"""


# ---------------------------------------------------------------
# BaseException - base class of all exceptions

e = BaseException("Hello", 1, 2, "test")
# e.args
print(e)


# ---------------------------------------------------------------
# Throw an exception

# raise SyntaxError("error happening...")       # after raise ... code unreachable
# raise "error"       # not possible (must inherit from BaseException class


# ---------------------------------------------------------------
# Catch an exception


def get0(name):
    return open(name, 'r')


def get(name):
    try:
        open(name, 'r')
    # except (FileNotFoundError, TypeError) as MajorFuckUp:     # without Error-Type, catch all Exceptions (bad)
    except FileNotFoundError:                                   # better use: 'except Exception'
        print("--- Some File Error Occurred ---")
        return None
    except TypeError:
        print("--- Some Type Error Occurred ---")
        return None
    finally:
        print("End")        # e.g. useful for closing stuff


def print_stuff():
    try:
        print([1, 2, 3][6])     # lst = [1, 2, 3] ... print(lst[6])
    except (IndexError, TypeError) as e:
        print("Error Message: ", e.args[0])


# ===========================================================================================
# test program:

def main_ex1():     # define main to make variable local and thus pycharm happy.
    name = 'tes.txt'
    name2 = [1, 2, 3]
    """
    for i in f:
        print("This is row: ", i)
    """
    return get(name2), get(name)


def main_ex2():
    return print_stuff()


print()
print("Example 1: ")
main_ex1()

print()
print("Example 2: ")
main_ex2()
