"""
Design Pattern Example: MVC - Package functions in single class

Oliver Zott
22.08.2019

TODO:   - what method static ???
        - why private ( "_item_type" ) ???
"""

import ModelViewController2.basic_backend as basic
import ModelViewController2.mvc_exceptions as mvc_exc


class ModelBasic(object):

    def __init__(self, application_items):
        self._item_type = 'product'                 # What for ??? (underscore to signal private)
        self.create_items(application_items)        # Whats that ???
        # self.item_type  --> instead property method

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        """
        Setter to @property decorator
        Accepts as argument a value, that user sets to the property (self.item_type)
        """
        self._item_type = new_item_type

    @staticmethod
    def create_item(name, price, quantity):     # why make static ???
        basic.create_item(name, price, quantity)

    def create_items(self, items):
        basic.create_items(items)

    def read_items(self):
        basic.read_items()

    def read_item(self, name):
        basic.read_item(name)

    def update_item(self, name, price, quantity):
        basic.update_item(name, price, quantity)

    def delete_item(self, name):
        basic.delete_item(name)


class View(object):

    def show_bullet_point_list(self, item_type, items):
        print(' ----- {} List -----'.format(item_type.upper()))
        for item in items:
            print('* {} '.format(item))


class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

