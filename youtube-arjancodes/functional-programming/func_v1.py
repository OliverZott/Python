"""
Functional programming example

"""
from datetime import datetime


def greet(name: str, greeting_intro: str) -> str:
    if name == "Olli":
        return "Hello"
    return f"{greeting_intro}, {name}."


# noinspection DuplicatedCode
def greet_list(names: list[str], greeting_intro: str) -> list[str]:
    # List Comprehension
    return [greet(name, greeting_intro) for name in names]


def get_greeting() -> str:
    current_time = datetime.now()
    if current_time.hour < 12:
        return "Good morning"
    elif 12 <= current_time.hour < 18:
        return "Good day"
    else:
        return "Good afternoon"


def read_name() -> str:
    return input("Enter your name: ")


def main() -> None:
    print(greet(read_name(), get_greeting()))
    print(greet_list(["Lena", "Olli"], get_greeting()))


if __name__ == "__main__":
    main()
