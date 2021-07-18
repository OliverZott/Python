from abc import ABC, abstractmethod


class Switchable(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):

    def turn_on(self):
        print("Light bulb: turned on...")

    def turn_off(self):
        print("Light bulb: turned off...")


class Fan(Switchable):

    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")


class ElectricPowerSwitch:
    def __init__(self, l: Switchable) -> None:
        self.switchable = l
        self.on = False

    def press(self):
        if self.on:
            self.switchable.turn_off()
            self.on = False
        else:
            self.switchable.turn_on()
            self.on = True


if __name__ == "__main__":
    l = LightBulb()
    f = Fan()
    switch = ElectricPowerSwitch(f)
    switch.press()
    switch.press()
