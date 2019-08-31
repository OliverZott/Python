"""
Design pattern - Model View Controller
Model - Part

source:     https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_model_view_controller.htm

Author:     Oliver Zott
Date:       07.08.2019
Version:    1.0
"""


class Person(object):
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    # returns Person name
    def name(self):
        return f"Name is '{self.first_name}', Surname is '{self.last_name}'."

    @classmethod
    def getAll(cls):
        """
        Returns all names in txt-file as list of person-objects
        """
        result = []     # same as result = list()
        with open('test.txt') as file:  # has to be in folder of main-file (controller)
            lines = file.readlines()
        for per in lines:
            person = Person(per.split(" ")[0], per.split(" ")[1].strip())   # strip gets rid of "\n"
            result.append(person)
        return result


# --------------------------------------------------------------
'''
Person1 = Person("Oliver", "Zott")
print(Person1.name())

# call class method (no instance needed)
print(Person.getAll())
'''
