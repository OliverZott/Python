class Employee:

    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
        # self.email = '{}.{}@mail.com'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@mail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name.')
        self.first = None
        self.last = None


if __name__ == "__main__":

    emp_1 = Employee('John', 'Smith')
    print(emp_1.email)
    emp_1.first = 'Jim'
    print(emp_1.email)
    emp_1.fullname = 'Olli Zott'

    print(emp_1.first)
    print(emp_1.email)
    print(emp_1.fullname)

    del emp_1.fullname
