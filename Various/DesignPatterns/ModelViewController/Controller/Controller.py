"""
Design pattern - Model View Controller
Controller - Part

source:     https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_model_view_controller.htm

Author:     Oliver Zott
Date:       07.08.2019
Version:    1.0
"""

from ModelViewController.Model import Person
from ModelViewController.View import showAllView
from ModelViewController import View


def showAll():
    # get list of all person objects
    people_in_db = Person.getAll()
    # calls view
    return showAllView(people_in_db)


def start():
    View.startView()
    inval = input()
    if inval == 'y':
        return showAll()
    else:
        return View.endView()


if __name__ == "__main__":
    start()
