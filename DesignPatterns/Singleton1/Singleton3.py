"""
Singleton - Example 3: simple implementation ?

-   raise Exception
-
-

(source: TutorialsPoint)

Author: Oliver Zott
Date: 19.09.2019
"""


class Singleton:
    __instance = None  # double underscore is sort of private (but not really)

    @staticmethod
    def get_instance():
        """
        Static Access Method!
        """
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """
        Virtually private constructor!
        """
        if Singleton.__instance is not None:
            raise Exception("This class is a Singleton!")
        else:
            Singleton.__instance = self


if __name__ == "__main__":
    s = Singleton()
    print(s)
    print()
    print(Singleton.get_instance())

    k = Singleton.get_instance()
    print(k)

    # s2 = Singleton()  # raises exception!
    # print(Singleton())

