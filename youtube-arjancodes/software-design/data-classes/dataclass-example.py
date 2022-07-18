from dataclasses import dataclass, field


class Person:
    name: str       # not necessary, normally only in initializer
    age: int        # not necessary, normally only in initializer
    job: str        # not necessary, normally only in initializer

    def __init__(self, name: str, age: str, job: str) -> None:
        self.name = name
        self.age = age
        self.job = job


@dataclass(order=True, frozen=True)
class Person2:
    # Sorting index
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    # Default values
    strength: int = 100

    def __post_init__(self):
        #self.sort_index = self.age
        # if frozen set is used, we have to initilize sort index other way:
        object.__setattr__(self, 'sort_index', self.age)

    # custom string representation

    def __str__(self) -> str:
        pass


if __name__ == "__main__":

    person1 = Person(name="Olli", job="Developer", age=37)
    person2 = Person(name="Leni", job="Marketing", age=34)
    person3 = Person(name="Sigi", age=3, job="Cuddeling")
    person4 = Person(name="Sigi", age=3, job="Cuddeling")

    person5 = Person2(name="Olli", job="Developer", age=37)
    person6 = Person2(name="Leni", job="Marketing", age=34)
    person7 = Person2(name="Sigi", age=3, job="Cuddeling")
    person8 = Person2(name="Sigiii", age=3, job="Cuddeling")

    print(id(person1))
    print(id(person2))
    print(person1)
    print(person3 == person4)
    # print(person3 > person4)
    print()

    print(id(person5))
    print(id(person6))
    print(person5)
    print(person7 == person8)
    print(person5 > person6)
    print()
