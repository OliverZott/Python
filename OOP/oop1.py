class Employee:

    number_of_employees = 0
    raise_amount = 1.03     # class variable

    def __init__(self, first, last, pay) -> None:
        self.first_name = first
        self.last_name = last
        self.pay = pay
        self.email = first + '.' + last + '@mail.com'
        Employee.number_of_employees += 1

    def __str__(self) -> str:
        return super().__str__() + ' / Name: ' + self.first_name + ' / E-Mail: ' + self.email

    def show_fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    """ Usage example for class variable """

    def apply_raise(self):
        # self.pay *= Employee.raise_amount   # to use the class raise-amount
        self.pay *= self.raise_amount   # to use the class raise-amount of then instance!?

    """ Class method """
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    """ Static method """
    @staticmethod
    def is_workday(day):
        if day.weekday() in {5, 6}:
            return False
        return True


if __name__ == "__main__":

    emp_1 = Employee('Olli', 'Zott', 47000)
    emp_2 = Employee('Lena', 'Bergmann', 52000)

    # -------------------------- Static methods --------------------------
    import datetime
    my_date = datetime.date(2021, 5, 21)
    
    print(Employee.is_workday(my_date))


    # -------------------------- Class and instance methods --------------------------
    # Employee.set_raise_amount(1.05)     # same as Employ.raise_amount = 1.05

    # -------------------------- Call and Use class variables --------------------------

    """
    First the own namespace (e.g. of instance) will be searched for the class-variable
    If not found, the class / or base class will be searched
    """
    # emp_1.raise_amount = 1.07

    """ found raise_amount on own namespace !!! """
    print(emp_1.raise_amount)
    """ no raise_amount in own namespace --> so it uses that from class """
    # print(emp_2.raise_amount)
    # print(Employee.raise_amount)

    # print(emp_1.pay)
    # emp_1.apply_raise()
    # print(emp_1.pay)

    # -------------------------- Calling instance methods with "self" keyword --------------------------
    # print(emp_2.show_fullname())
    # Employee.show_fullname(emp_2)

    # print(emp_1.__sizeof__())
    # print(emp_2.__str__())
