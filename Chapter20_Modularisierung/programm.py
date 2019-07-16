"""
USE of Packages and Modules / __init__.py

https://docs.python.org/3/reference/import.html#regular-packages
https://stackoverflow.com/questions/448271/what-is-init-py-for

Created on 29.04.2019
@author: Dura
"""


import mathehelfer                                              # Modules used:    mathehelfer.fak()
# gesamter Modulinhalt in Namensraum einbinden -evtl unerwuenschte effekte --> from ... import ...
from mathehelfer import kehr                                    # Modules used:    kehr()
import Paket_IO.py_in       # need of __init__ in sub folder to import packet (but empty init file!)
import fibonacci                                                # use of __init__ in sub folder !!!


# --------------------------------------------------------------------------------------------------
# Test for Module / packet references 
# --------------------------------------------------------------------------------------------------

print("------------------------------------------")
print("Print import_Paket_IO NAME: ")
print(Paket_IO.__name__)
print("Print import_Paket_IO PATH: ")
print(Paket_IO.__file__)
print("")

print("------------------------------------------")
print("Print import_Paket_IO.py_in NAME: ")
print(Paket_IO.py_in.__name__)
print("Print import_Paket_IO.py_in PATH: ")
print(Paket_IO.py_in.__file__)
print("")


print("------------------------------------------")
print("Print import_fib.rec NAME: ")
print(mathehelfer.__name__)
print("Print import_fib.rec PATH: ")
print(mathehelfer.__file__)
print("")
print("------------------------------------------")


# --------------------------------------------------------------------------------------------------
# Call of Module in same directory 
# --------------------------------------------------------------------------------------------------

print("Fakultaet : ", mathehelfer.fak(7))
print("")
print("Kehrwert: ", kehr(346))
print("")


# --------------------------------------------------------------------------------------------------
# Call of Module in different directory (sub-folder) WITHOUT  __init__
# --------------------------------------------------------------------------------------------------

zahl = Paket_IO.py_in.user_input_int()

print(zahl)

# --------------------------------------------------------------------------------------------------
# Call of Module in different directory (sub-folder) WITH  __init__
# --------------------------------------------------------------------------------------------------

print("------------------------------------------")
# print ("Fibonacci with fib2(): ", fibonacci.fib2.fib_2(zahl))     # still need the fib2 filename declaration?
print("")
print("Fibonacci with fib_1(): ", fibonacci.fib_1(zahl))            # here we already imported fib1 via __init__ file!
print("")
print("Fibonacci with fib_rec(): ", fibonacci.fib_rec(zahl))
print("")

print("------------------------------------------")
