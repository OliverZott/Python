import requests


class Employee:
    """"Sample employee class"""

    raise_percentage = 1.2

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f"{self.first}.{self.last}@mail.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay *= self.raise_percentage

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'

    def __repr__(self):
        return f"{self.fullname} earns {self.pay}$."


class Developer(Employee):
    raise_percentage = 1.3


if __name__ == "__main__":
    emp1 = Employee('John', 'Doe', 10000)
    dev1 = Developer('Mack', 'Knife', 10000)

    print(emp1)
    print(dev1)
    emp1.apply_raise()
    dev1.apply_raise()

    print(emp1)
    print(dev1)
