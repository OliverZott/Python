"""
run AST:
    python -m ast <filename>
"""


def function1():
    return "{}{}".format("Hello", "World")


def function2():
    return f'{"Hello "}{"World"}'


def main():
    print(function1())
    print(function2())


if __name__ == '__main__':
    main()
