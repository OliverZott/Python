""""
Chapter23 OOP: Example 1

- __init__
- @property
- .setter


source:
 - https://fabienmaussion.info/scientific_programming/html/23-OOP-Part-1.html

@author Oliver Zott
@date 2019-12-10
"""


class Cat:

    # class-attribute
    cat_speak = 'Meow'

    def __init__(self, name, weight, language='en'):
        # instance attributes
        self.name = name
        self.weight = weight
        self.speak = None  # decided by _decide_speech method!
        self._language = None  # private attribute
        self.language = language

    def say_name(self):
        print('{}, says {} Cat'.format(self.speak, self.name))
        print(f'{self.name} says {self.speak}')  # newer python format version

    def _decide_speech(self, value):
        """
        Private method:
        used to structure code in our class
        :param value:
        """
        if value == 'en':
            self.speak = 'Meow'
        elif value == 'fr':
            self.speak = 'Miaou'
        elif value == 'de':
            self.speak = 'Moin Moin!'
        else:
            raise ValueError('Language not understood: {}'.format(value))

    def eat_food(self, food_kg):
        """
        function to feed cat
        CAREFUL: function changes instance attribute during object lifetime

        @param food_kg: float
        """
        self.weight += food_kg

    # Property getter
    @property
    def language(self):
        return self._language

    # Property setter
    @language.setter
    def language(self, value):
        self._language = value
        self._decide_speech(value)

    @property  # use method like it was attribute
    def weight_lbs(self):
        """
        alternative versions (worse!):
            - self.weight_lbs in __init__  BUT... what if cat eats food?  lbs not updated!
            - write own get_ method  BUT... but hides fact, that it is still an attribute!

        better: @property
        """
        return self.weight / 0.45359237

    # property setter
    @weight_lbs.setter
    def weight_lbs(self, new_weight):
        """
        alternative (worse!): new setter set_weight_lbs(self, new_weight)
            but: now obj.set_xxx() ... instead obj.xxx = new_value  (attribute style)
        """
        self.weight = 0.45359237 * new_weight


if __name__ == "__main__":

    kosto = Cat("Kostolany", 4)
    kosto.say_name()
    kosto.language = 'fr'
    print(kosto.language)
    kosto.say_name()

    """
    # 23.1 Some basics
    a = Cat('Grumpy', 4)
    print(a)  # created instance of CAT class
    print(isinstance(a, Cat))
    print(type(Cat))
    print(type(a))
    a.say_name()

    b = Cat('Grumpy', 4)
    print(a is b)
    print(a == b)

    # 23.5  @property
    print("\n@property example: ")
    print('Weight before eat: {:.3f} kg'.format(a.weight))  # formatting float
    a.eat_food(0.2)
    print('Weight after eat: {:12.1f} kg'.format(a.weight))
    print(a.weight_lbs)

    # 23.6
    ''' consistent syntax thanks to 
    @property           ... method as attribute
    @pro_obj.setter     ... setter for property (used as attribute)
    '''
    c = Cat('Kosto', 5)
    c.eat_food(0.4)
    print("c.weight: ", c.weight, "; c.weight_lbs:", c.weight_lbs)
    c.weight_lbs = 3
    print(c.weight, c.weight_lbs)
    c.speak
    """

