"""
Exception Handling Example 2

Oliver Zott
16.07.2019
"""


class Account:
    def __init__(self, balance):
        self.balance = balance
        self.withdrawn = 0.0

    def withdraw(self, value):
        if value > self.balance:
            raise AccountException(self.balance, value)
        self.balance -= value
        self.withdrawn -= value
        Account.show(self)

    def show(self):
        print("Balance: ", self.balance)
        print("Withdrawn: ", self.withdrawn)
        print()


# subclass of Exception-class
class AccountException(Exception):
    def __init__(self, balance, value):
        self.Balance = balance
        self.Value = value

    def __str__(self):
        return "balance too low"


# ===========================================================================================
# test program:

# acc = Account(1265)
# acc.withdraw(100)

acc2 = Account(4999)
acc2.withdraw(50000)
