""" Dataclass example 

https://www.youtube.com/watch?v=vRVVyl9uaZc&list=PLC0nd42SBTaMpVAAHCAifm5gN2zLk2MBo&index=3

Remarks:
- order
- field 
    - sort_index is not a "setable" field --> init false
    - not part of to-string method --> repr false
- frozen ...readonly
- __str__ 

"""

from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class DataPerson:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        # order-field setting if not frozen!
        # self.sort_index = self.age

        # order-field workaround if class is frozen!
        object.__setattr__(self, 'sort_index', self.strength)

    def __str__(self) -> str:
        return f'{self.name}, {self.job} ({self.age})'


data_person1 = DataPerson("Name1", "Job1", 25, 99)
data_person2 = DataPerson("Name2", "Job2", 30)
data_person3 = DataPerson("Name2", "Job2", 30)
# data_person1.age = 123  # not working if dataclass is FROZEN


class Person:

    def __init__(self, name, job, age) -> None:
        self.name = name
        self.job = job
        self.age = age


person1 = Person("Name1", "Job1", 25)
person2 = Person("Name2", "Job2", 30)
person3 = Person("Name2", "Job2", 30)

print(person1)
print(id(person2))
print(id(person3))
print(person2 == person3)

print(" ------------------------------------------------------------------ ")

print(data_person1)
print(data_person3)
print(id(data_person2))
print(id(data_person3))
print(data_person2 == data_person3)
print(data_person1 > data_person2)
