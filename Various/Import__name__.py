"""
Python Main: __name__

sources:
- https://www.geeksforgeeks.org/__name__-special-variable-python/
- https://stackoverflow.com/questions/419163/what-does-if-name-main-do

Oliver Zott
21.08.2019
"""


from __name__ import File1

print("File2 __name__ = {}".format(__name__))

print()
print("FunctionB call from File1:")
File1.functionB()
