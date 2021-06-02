"""
Test Application for MVC - CRUD - Project

"""

from ModelViewController2 import model_view_controller as mvc


def start():

    my_items = [
        {'name': 'bread', 'price': 1.2, 'quantity': 17},
        {'name': 'beer', 'price': 1.8, 'quantity': 20}
    ]

    c = mvc.Controller(mvc.ModelBasic(my_items), mvc.View)

    c.show_items()


if __name__ == "__main__":
    start()
