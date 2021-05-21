class Employee: 

    raise_amt = 1.04

    def __init__(self, first,last,pay) -> None:
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@mail.com'
        self.pay = pay

    def fullName(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __str__(self) -> str:
        return self.first + ' ' + self.last + ' earns ' + str(self.pay) + ' "monies". '

class Developer(Employee):
    pass



if __name__ == "__main__":
    dev1 = Developer("vn1", "nm1", 1)
    dev2 = Developer("vn2", "nm2", 2)

print(help(Developer))

print(dev1)
print(dev2)
