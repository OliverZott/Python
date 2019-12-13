""""
Chapter23 OOP: Example 1

- __init__
-


source:
 - https://fabienmaussion.info/scientific_programming/html/23-OOP-Part-1.html

@author Oliver Zott
@date 2019-12-10
"""


class Cat:
    """
    First example: cat class
    """

    # class-attribute
    speak = 'Meow'

    # initializer
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    # method 1
    def say_name(self):
        """
        Method for cat-class
        """
        print('{}, says {} Cat'.format(self.speak, self.name))
        print(f'{self.name} says {self.speak}')  # newer python format version

    # method 2
    def eat_food(self, food_kg):
        """
        function to feed cat
        CAREFUL: function changes instance attribute during object lifetime

        @param food_kg: float
        """
        self.weight += food_kg

    # attribute (property)
    @property
    def weight_lbs(self):
        """
        alternative versions (worse!):
            - self.weight_lbs in __init__  BUT... what if cat eats food?  lbs not updated!
            - write own get_ method  BUT... but hides fact, that it is still an attribute!

        better: @property
        """
        return self.weight / 0.45359237


if __name__ == "__main__":

    # 23.1 Some basics
    a = Cat('Grumpy', 4)
    print(a)  # created instance of CAT class
    print(isinstance(a, Cat))
    print(type(Cat))
    print(type(a))
    print(a.say_name())

    b = Cat('Grumpy', 4)
    print(a is b)
    print(a == b)

    # 23.5  @property
    print('Weight before eat: {:.3f} kg'.format(a.weight))  # formatting float
    a.eat_food(0.2)
    print('Weight after eat: {:12.1f} kg'.format(a.weight))
    print(a.weight_lbs)

