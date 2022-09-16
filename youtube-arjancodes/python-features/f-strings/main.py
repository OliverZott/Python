""" 
https://www.youtube.com/watch?v=Mfmr_Puhtew

- __str__ for users (dataclass default output if exists, else repr)
- __repr__ for devs
-

"""

import datetime
from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class User2:
    def __init__(self, firstName: str, lastName: str) -> None:
        self.first_name = firstName
        self.last_name = lastName


def main():

    # dataclasses
    user1 = User("John", "Doe")
    user2 = User2("Jane", "Doe")
    # printing calls __str__, if it doesn't exist, __repr__ is used!
    print(f"User1: {user1}")    # uses __str__ (the user firendly output)
    print(f"User1: {user1!r}")  # uses __repr__ (the dev firendly output)
    print(f"User1: {repr(user1)}")
    print(f"User2: {user2}\n")

    # Number formats
    number = 100.2476458456
    # print(f"Number (scientific): {number:e}.")
    # print(f"Number (decimals and round): {number:.2f}.")
    # print(f"Number: {number}.")
    # print(f"Number (hex): {100:x}.")
    # print(f"Number (total char number): {100:06}.")
    # print(f"Number (number as percent): {0.024235555:.3%}.\n")

    # Debugging variables
    x = 123
    y = 42
    print(f"{ x = }{y=}")

    # Dict
    dictionary = {"key1": "value1", "key2": "value2"}
    # print(f"Dict: value1={dictionary['key1']}")
    # print(
    #     f"Dict: key2={list(dictionary.keys())[list(dictionary.values()).index('value2')]}")

    # Date formats
    today = datetime.datetime.now()
    print(today)
    print(f"{today:%H:%M:%S:%f}")

    # Align numbers and text
    # print(f"Number (align): {123:12}.")
    # print(f"Text (align right): {'blub':>12}.")
    # print(f"Text (align center): {'blub':^12}.")
    # print(f"Text (align right with underscore): {'blub':_<12}.\n")


if __name__ == "__main__":
    main()
