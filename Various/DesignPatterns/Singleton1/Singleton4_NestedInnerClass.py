"""
Singleton - Example 4:  Nested Inner Class

-   Nested Inner Classes
-   repr()
-   __str__
-   __getattr__
-   getattr

(source: Python 3 Patterns, Recipes and Idioms)

Author: Oliver Zott
Date: 19.09.2019
"""


class OnlyOne:

    class __OnlyOne:  # nested inner class; __ makes it private, cannot access it directly

        def __init__(self, arg):
            self.val = arg

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg

    def __getattr__(self, item):
        return getattr(self.instance, item)


if __name__ == "__main__":

    x = OnlyOne("sausage")
    print(x)
    y = OnlyOne("eggs")
    print(y)
    z = OnlyOne("ham")
    print(z)

