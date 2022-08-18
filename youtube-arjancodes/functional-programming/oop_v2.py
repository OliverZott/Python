"""
Functional programming example

Removed side effects to other place (main function) --> can unit test now

Goal:
- at some points always side effects --Y at least group somewhere!

Better:
- all functions are predictable / only depend on provided inputs
- functions return stuff, so easier to test
- functions have lesser dependencies -> dependencies as arguments

Problems:
- main function still has all the problems from before
"""
from datetime import datetime


class Greeting:

    def __init__(self, greeting_intro: str) -> None:
        self.greeting_intro = greeting_intro

    def greet(self, name: str) -> str:
        return f"{self.greeting_intro}, {name}."

    def greet_list(self, names: list[str]) -> list[str]:
        greetings: list[str] = []
        for name in names:
            greetings.append(self.greet(name))
        return greetings


def main() -> None:
    current_time = datetime.now()
    if current_time.hour < 12:
        greeting_intro = "Good morning"
    elif 12 <= current_time.hour < 18:
        greeting_intro = "Good day"
    else:
        greeting_intro = "Good afternoon"

    name = input("Enter your name: ")

    greeting = Greeting(greeting_intro)
    greeting.greet(name)


if __name__ == "__main__":
    main()
