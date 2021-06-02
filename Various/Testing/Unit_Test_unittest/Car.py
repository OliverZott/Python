"""
Pycharm Tutorial
source: https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html

- Code
- Debug
- Test
- Django Framework

author: Oliver Zott
date: 2019-12-11
"""


class Car:
    """
    Class implementing a car thing
    Functions: accelerate, break ...
    """

    def __init__(self, speed=0):
        """
        constructor of car object
        :param speed:
        """
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_statement(self):
        print("I'm going {} kph and drove for {}".format(self.speed, self.time))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass


if __name__ == "__main__":

    my_car = Car()
    print("I'm a car")
    print(help(my_car))
    print()
    print(Car.__doc__)

    while True:
        action = input("What should I do? [A]ccelerate, [B]reake,"
                       "shoe [O]dometer, show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know what to do?!")
            continue
        elif action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} km".format(my_car.odometer))
        elif action == 'S':
            print("The average speed is {} kph".format(my_car.average))
        my_car.step()
        my_car.say_statement()

