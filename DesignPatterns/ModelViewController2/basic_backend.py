"""
Design Pattern Example: MVC -  (Model View Controller)

goals:
- CRUD - persistent storage
- https://www.python-kurs.eu/lambda.php


sources:
- https://www.giacomodebidda.com/mvc-pattern-in-python-introduction-and-basicmodel/
- https://www.hsg-kl.de/faecher/inf/python/oop/mvc/index.php
- https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/

Oliver Zott
21.08.2019

TODO:   - Error-Logging
"""


from ModelViewController2 import mvc_exceptions as mvc_exc


# global variable; can be shared across all operation (declared outside a function)
items = list()


# create
def create_item(name, price, quantity):
    global items
    checking = list(filter(lambda x: x['name'] == name, items))
    if checking:
        raise mvc_exc.ItemAlreadyStored('Item already stored !!!')
    else:
        items.append({'name': name, 'price': price, 'quantity': quantity})


# create items-list from arbitrary dictionary list
def create_items(app_items):
    global items    # global keyword to change global variable from inside a function
    items = app_items


# read
def read_item(name):
    global items
    my_list = list(filter(lambda x: x['name'] == name, items))
    if my_list:
        return my_list[0]
    else:
        raise mvc_exc.ItemNotStored('Item "{}" not stored !!!'.format(name))


def read_items():
    global items
    return (item for item in items)


# update
def update_item(name, price, quantity):
    global items
    idxs_items = list(filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i, item_to_update = idxs_items[0][0], idxs_items[0][1]
        items[i] = {'name': name, 'price': price, 'quantity': quantity}
    else:
        raise mvc_exc.ItemNotStored('Can\'t update item "{}", because it\'s not stored'.format(name))


# delete
def delete_item(name):
    global items
    idxs_items = list(filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))  # WHY IS THIS WORKING ???
    if idxs_items:
        i, item_to_update = idxs_items[0][0], idxs_items[0][1]
        del items[i]
    else:
        raise mvc_exc.ItemNotStored('Can\'t delete item "{}", because it\'s not stored'.format(name))


# ---------------------------------------------------------------------
# testing with main:


def main():
    my_items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 0.9, 'quantity': 35},
        {'name': 'wine', 'price': 6.9, 'quantity': 9}
    ]

    create_items(my_items)

    create_item('banana', 0.89, 154)
    create_item('apple', 0.34, 98)
    create_item('strawberry', 0.12, 5346)
    # create_item('banana', 0.29, 123)
    print(items)

    print()
    print("Update strawberry: ")
    update_item('strawberry', 0.12, 500)
    print(read_item('strawberry'))

    print()
    print("Delete apple: ")
    delete_item('apple')
    # update_item('peach', 0.24, 27)
    # print(read_item('peach'))
    print(items)


if __name__ == '__main__':
    main()
