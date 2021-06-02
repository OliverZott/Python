"""
Design Pattern Example: MVC - Package functions in single class
MODEL part

Oliver Zott
22.08.2019

TODO:   - what method static ???
        - why private ( "_item_type" ) ???
"""

import ModelViewController2.basic_backend as basic
import ModelViewController2.mvc_exceptions as mvc_exc


# -----------------------------------------------------------------------------------
# MODEL
class ModelBasic(object):

    def __init__(self, application_items):
        self._item_type = 'product'                     # underscore to signal private
        self.create_items(application_items)            # Whats that ???
        # self.item_type  --> instead property method

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type

    @staticmethod
    def create_item(name, price, quantity):     # why make static ???
        basic.create_item(name, price, quantity)

    @staticmethod
    def create_items(items):
        basic.create_items(items)

    @staticmethod
    def read_items():
        basic.read_items()

    @staticmethod
    def read_item(name):
        basic.read_item(name)

    @staticmethod
    def update_item(name, price, quantity):
        basic.update_item(name, price, quantity)

    @staticmethod
    def delete_item(name):
        basic.delete_item(name)


# -----------------------------------------------------------------------------------
# VIEW
# no logic / only static / no mention of other components!
# -> for fancy view: just implement new "view" class!

class View(object):

    @staticmethod
    def show_bullet_point_list(item_type, items):
        print('--- {} LIST ---'.format(item_type.upper()))
        for item in items:
            print('* {}'.format(item))


def show_number_point_list(item_type, items):
    print('--- {} LIST ---'.format(item_type.upper()))
    for _i, item in enumerate(items):
        print('{}. {}'.format(_i + 1, item))


# -----------------------------------------------------------------------------------
# CONTROLLER
class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_items(self, bullet_points=False):
        items = self.model.read_items()
        item_type = self.model.item_type
        if bullet_points:
            self.view.show_bullet_point_list(item_type, items)
        else:
            show_number_point_list(item_type, items)


# ----------------------------------------------------------------------------------
# test
my_items = [
    {'name': 'bread', 'price': 0.5, 'quantity': 20},
    {'name': 'milk', 'price': 1.0, 'quantity': 10},
    {'name': 'wine', 'price': 10.0, 'quantity': 5},
]

c = Controller(ModelBasic(my_items), View())

show_number_point_list('product', my_items)


print(" -----------------------------------------")
c.show_items()


print(type(my_items))
for i in my_items:
    print(i)
