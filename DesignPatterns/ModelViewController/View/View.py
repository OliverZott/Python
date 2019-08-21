"""
Design pattern - Model View Controller
View - Part

source:     https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_model_view_controller.htm

Author:     Oliver Zott
Date:       07.08.2019
Version:    1.0
"""

from ModelViewController.Model import Person       # to make work shift+alt+F10 uncheck 2 PYPATH boxes


def showAllView(list):
    print(f'In our txt we have: {len(list)} persons. They are:')
    for item in list:
        print(item.name())


def startView():
    print('MVC - simple example')
    print('Wanna see everyone? [Y/N]')


def endView():
    print('Bye!')
