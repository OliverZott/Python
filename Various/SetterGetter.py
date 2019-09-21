"""
Example: Setter/Getter, Instance- vs ClassVariables

see also Java Example:

-   why can still call/set Shark2._name ???

Author: Oliver Zott
Date: 19.09.2019
"""


class Shark(object):
    """
    class without setter/ getter
    """
    type = "fish"   # class variable (for all clas objects the same)

    def __init__(self, name: str = None, age: int = 0):
        self.name = name    # instance variables (each instance has different instance variables)
        self.age = age


class Shark2(object):
    """
    Class with setter / getter
    @property
    """
    type = "fish with set/get"

    def __init__(self):
        self._name = None
        self._age = 0

    @property
    def attr(self):
        print("Getter Method of Shark2-Class")
        return self._name, self._age

    @attr.deleter
    def attr(self):
        self._age = None
        self._name = None

    @property
    def name(self):
        print("Getter Method of Shark2-Class")
        return self._name

    @name.setter
    def name(self, value):
        if type(value) == str:
            self._name = value
        else:
            print("Name must be of type string")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if type(value) == int:
            self._age = value
        else:
            print("Age must be of type int")


class Shark3(object):
    """
    Class with setter / getter
    set_func, get_func, property()
    """

    def __init__(self):
        self._name = "Shark3-insctance"
        self._age = "shark3-instance-age"

    def get_attr(self):
        return self._name, self._age

    def set_attr(self, name, age):
        if type(name) == str:
            self._name = name
        else:
            print("name type error")
        if type(age) == int:
            self._age = age
        else:
            print("age type error")


if __name__ == "__main__":

    # -------------------------------
    # Example 3
    shark31 = Shark3()

    shark32 = Shark3()
    shark32.set_attr("Leni", 31)
    shark33 = Shark3()
    shark33.set_attr(34, "bl")
    shark33._name = "bl"
    

    print("Get attributes standard way: Name: {}, Age: {}".format(shark31._name, shark31._age))
    print()
    name, age = shark32.get_attr()
    print("Get attributes GETTER way: Name: {}, Age: {}".format(name, age))
    print()
    print(shark33.get_attr())
    #print("Get attributes GETTER way: Name: {}, Age: {}".format(shark32.get_attr()))

    '''
    # -------------------------------
    # Example 2
    shark1 = Shark2()

    shark2 = Shark2()
    shark2.name = "Olli"
    shark2.age = 36
    shark2._name = "bla"

    print("Get attributes standard way: Name: {}, Age: {}".format(shark1._name, shark1._age))
    print()
    print("Get attributes GETTER way: Name: {}, Age: {}".format(shark2.name, shark2.age))
    '''

    '''
    # -------------------------------
    # Example 1
    shark1 = Shark("olli", 36)
    shark_def = Shark()

    shark2 = Shark(23, "fde")

    print(shark1)
    print(shark2.age)
    print(shark_def.type)
    '''


