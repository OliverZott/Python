class Employee:
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

    def __str__(self) -> str:
        return self.first + ' ' + self.last + ' earns ' + str(self.pay) + ' "monies". '


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)   # for Mltiple Inheritance
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        return self

    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.full_name())


if __name__ == "__main__":
    emp1 = Employee('vn1', 'nm1', 40000)
    dev1 = Developer('vn2', 'nm2', 50000, 'Python')
    dev2 = Developer('vn3', 'nm3', 50000, 'Java')
    man1 = Manager('vn2', 'nm2', 100000, [dev2])

    print(isinstance(man1, Developer))
    print(issubclass(Developer, Employee))

    man1.add_emp(emp1).add_emp(dev1)
    man1.print_emps()


# print(help(Developer))
# print(Developer.mro())


# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)
