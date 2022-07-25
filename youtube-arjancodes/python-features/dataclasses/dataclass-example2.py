"""
Dataclasses example
https://www.youtube.com/watch?v=CvQ7e6yUtnw


Remarks:
- __init__ and __repr__ autogenerated
- Fields:
    - default values
    - Factory method
    - restrictions -> init=False
    - private vs pulbic -> repr=False
- frozen=True ...readonly after initialization - immutable
    - python has NO concept for constants (const) for primitive types !!!
- kw_only=True ... only instatiate with keyword arguments
- match_args=True ...for structural pattern matching
    - creates match args dunder method to supply arguments for structural pattern matching
- slots=True ...using slots (faster) instead of __dict__ dunder object

Downside:
- Abuse class-variable concept to describe instance-variables
"""

import random
import string
from dataclasses import dataclass, field


def generate_id():
    return "".join(random.choices(string.ascii_uppercase, k=12))


class Person_Simple():
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}, {self.age}"


@dataclass(frozen=False, kw_only=True, match_args=True)
class Person():
    name: str
    age: int
    biker: bool = True
    # python uses references -> each instance same list ref !!
    # email_addresses = list[str] = []
    email_addresses: list[str] = field(default_factory=list)
    id: str = field(init=False, default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._search_string = f"{self.name} {self.age}"


def main():
    person1 = Person(name="Olli", age=30)
    person2 = Person(name="Sigi", age=20, biker=False)

    # person3 = Person(name="Olli", age=30, id="asdf")  # not working: init=False
    print(person1)

    # Frozen
    # person2.name = "John"
    print(person2)


if __name__ == "__main__":
    main()
