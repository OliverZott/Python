"""
Dont call function!!
dis.dis(function1)

--> f-string faster than .format() !!
"""

import dis


def function1():
    return "{} {}".format("Hello", "World")


def function2():
    return f'{"Hello"} {"World"}'


def main():
    dis.dis(function1)  # NO function call !!!
    dis.dis(function2)


if __name__ == '__main__':
    main()
