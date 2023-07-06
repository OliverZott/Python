# Always raises infinite loop
import sys
from typing import NoReturn


# Returns "None"
def func1() -> None:
    print("Hello from func1")


# no return if exit, exception, ...
def func2() -> NoReturn:
    print("Hello from func2")
    sys.exit(-1)  # no implicit return!


def main() -> None:
    func1()
    func2()


if __name__ == "__main__":
    main()
