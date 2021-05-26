class Employee:
    """
    Resource: https://www.youtube.com/watch?v=3ohzBxoFHAY&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=5
    """
    raise_amt = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@mail.com'
        self.pay = pay

    def full_name(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self) -> str:
        return "Employee('{}', '{}', {})". format(self.first, self.last, self.pay)

    def __str__(self) -> str:
        return '{} - {}'.format(self.full_name(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())


if __name__ == "__main__":

    emp_1 = Employee("Olli", "Zott", 100)
    emp_2 = Employee("Ingo", "Cnito", 150)

    print(len(emp_1))

    # print(emp_1+emp_2)

    # print(1+2)
    # print('a'+'b')
    # print(str.__add__('a', 'b'))

    # print(repr(emp_1))
    # print(str(emp_1))
    # print(emp_1.__repr__())
    # print(emp_1)
