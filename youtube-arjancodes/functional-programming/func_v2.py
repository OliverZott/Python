"""
Functional programming example with
- Delegates??
- "Partial function application"

"""
from datetime import datetime
from typing import Callable
from functools import partial

# REMARK: Same as Delegates in C# ?
GreetingReader = Callable[[], str]
GreetingFunction = Callable[[str], str]


def greet(name: str, greeting_reader: GreetingReader) -> str:
    if name == "John":
        return "Hello"
    return f"{greeting_reader()}, {name}."


# noinspection DuplicatedCode
def greet_list(names: list[str], greeting_reader: GreetingReader) -> list[str]:
    # REMARK: List Comprehension
    return [greet(name, greeting_reader) for name in names]


def greet_list2(names: list[str], greeting_fn: GreetingFunction) -> list[str]:
    # REMARK: List Comprehension
    return [greeting_fn(name) for name in names]


def get_greeting() -> str:
    current_time = datetime.now()
    if current_time.hour < 12:
        return "Good morning"
    elif 12 <= current_time.hour < 18:
        return "Good day"
    else:
        return "Good afternoon"


def get_greeting_new() -> str:
    return "Hi there, "


def read_name() -> str:
    return input("Enter your name: ")


def main() -> None:
    # REMARK: Partial function application
    greet_fn = partial(greet, greeting_reader=get_greeting_new)
    print(greet_fn("All"))

    # REMARK: Now don't call function for "get_greeting", provide as argument!!
    print(greet(read_name(), get_greeting))
    print(greet_list(["Lena", "Olli"], get_greeting))

    print(greet_list2(["Lena", "Olli"], greet_fn))


if __name__ == "__main__":
    main()
