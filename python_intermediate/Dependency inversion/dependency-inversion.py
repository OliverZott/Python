class LightBulb:
    def turn_on(self):
        print("Light bulb: turned on...")

    def turn_off(self):
        print("Light bulb: turned off...")


class ElectricPowerSwitch:
    def __init__(self, l: LightBulb) -> None:
        self.lightbulb = l
        self.on = False

    def press(self):
        if self.on:
            self.lightbulb.turn_off()
            self.on = False
        else:
            self.lightbulb.turn_on()
            self.on = True


if __name__ == "__main__":
    l = LightBulb()
    switch = ElectricPowerSwitch(l)
    switch.press()
    switch.press()
