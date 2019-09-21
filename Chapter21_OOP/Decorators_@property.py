"""
Example for @property Decorator / using setter

https://www.machinelearningplus.com/python/python-property/
https://www.programiz.com/python-programming/property
https://www.python-course.eu/python3_properties.php

0.  Pythonic way to user set / get --> @property

1.  When to use @property decorator?
    When an attribute is derived from other attributes in the class,
    so the derived attribute will update whenever the source attributes is changed.

2.  How to make a @property?
    Make an attribute as property by defining it as a function and
    add the @property decorator before the fn definition

3.  @property lets a method to be accessed as an attribute instead of as a method with funcftion call '()'.

4.  When to define a setter method for the property?
    Typically, if you want to update the source attributes whenever the property is set.
    It lets you define any other changes as well.

source:     https://python-textbok.readthedocs.io/en/1.0/Classes.html#class-decorators
            https://python-textbok.readthedocs.io/en/1.0/Functions.html#decorators
            https://www.programiz.com/python-programming/property

Author:     Oliver Zott
Date:       23.07.2019
"""


class Person(object):
    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname
        # self.fullname = self.firs + ' ' + self.last     # won't show correct full name after changing first or last!

	# property decorator for getter-method also used!
	
    @property       # fullname used as an attribute
    def fullname(self):
        """
        - to change full name, when changing first/last attributes --> declare as method
        - to still use fullname without () --> declare property with @property!
        """
        return self.first + ' ' + self.last

    @fullname.setter
    def fullname(self, name):
        """
        -  the setter method should have the same name as the equivalent method that @property decorates.
        -  it accepts as argument the value that user sets to the property.
        """
        fisrname, lastname = name.split()
        self.first = fisrname
        self.last = lastname

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)


# ========================================================================================================
# Instance creation and testing

olli = Person('Oliver', 'Zott')
print(olli.last)
print(olli.fullname)
print(olli.email())     # uses () after calling method!
print()

olli.last = 'Bergmann'
print(olli.last)
print(olli.fullname)    # fullname attribute didn't change after changing other attribute --> make it method (line36)
print(olli.email())     # method changed
print()

# try change fullname Attribute
olli.fullname = 'Ollgu Zwuu'    # throws AttributeError!
# using setter to handle that problem (line44)
print(olli.fullname)
print(olli.email())
print()

# try deleter
del olli.fullname

print(olli.first)
print(olli.last)
