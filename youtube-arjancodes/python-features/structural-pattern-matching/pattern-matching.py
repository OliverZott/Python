"""
Example app for structural pattern matching (Python 3.10)

(https://www.youtube.com/watch?v=scNNi4860kk&list=PLC0nd42SBTaMpVAAHCAifm5gN2zLk2MBo)

Pattern matching with ...
- split strings
- conditions
- objects (on the attributes of the object)


Remarks:
- different to switch-case in other languages:
    - python breaks if case hits
    - no default case (instead use _ )

Caveats:
- Order of cases is important!
- Looks like "switch-case" which may lead to bad design decisions!
"""

from dataclasses import dataclass
from typing import List
import shlex


def run_command(command: str) -> None:
    match command:
        case "quit":
            print("Quitting app!")
            quit()
        case "reset":
            print("resetting app!")
        case other:
            print(f"Other stuff: {other!r}.")


def run_command_v2(command: str) -> None:
    """
    Pattern matching with string-split
    """
    match command.split():
        case ["load", filename]:
            print(f"Loading file {filename}.")
        case ["save", filename]:
            print(f"Saving file {filename}.")
        case ["exit" | "quit" | "bye", *rest]:
            if "--force" in rest or "-f" in rest:
                print(f"Forcing program quit!")
            print("Quitting app!")
            quit()
        case _:
            print(f"Other stuff: {command!r}.")


def run_command_v3(command: str) -> None:
    """
    Pattern matching with conditions
    """
    match command.split():
        case ["load", filename]:
            print(f"Loading file {filename}.")
        case ["save", filename]:
            print(f"Saving file {filename}.")
        # if-condition as part of pattern matching --> adding condition to cases!
        case ["exit" | "quit" | "bye", *rest] if "--force" in rest or "-f" in rest:
            print(f"Forcing program quit!")
            quit()
        case ["exit" | "quit" | "bye"]:
            print("Quitting app!")
            quit()
        case _:
            print(f"Other stuff: {command!r}.")


@dataclass
class Command:
    command: str
    arguments: List[str]


def run_command_v4(command: Command) -> None:
    """
    Pattern matching for objects / attributes
    """
    match command:
        case Command(command="load", arguments=[filename]):
            print(f"Loading file {filename}.")
        case Command(command="save", arguments=[filename]):
            print(f"Saving file {filename}.")
        case Command(command="exit" | "quit" | "bye", arguments=["--force" | "-f", *rest]):
            print(f"Forcing program quit!")
            quit()
        case Command(command="exit" | "quit" | "bye"):
            print("Quitting app!")
        case _:
            print(f"Unknown command: {command!r}.")
            print(f"Unknown command: {command}.")


def main() -> None:
    while True:
        # command = input("input plz:")
        command, *arguments = shlex.split(input("$ "))
        run_command_v4(Command(command, arguments))


if __name__ == "__main__":
    main()
