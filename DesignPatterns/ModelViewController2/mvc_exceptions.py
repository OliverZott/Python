"""
Design Pattern Example: MVC - Exception Handling

Oliver Zott
21.08.2019
"""


# Custom exceptions derived from basic Exception Class
class ItemAlreadyStored(Exception):
    pass


class ItemNotStored(Exception):
    pass
