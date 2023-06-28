# Dunder Methods

In Python, dunder methods are methods that allow instances of a class to interact with the built-in functions and operators of the language.

## Basic Customizations

- `__new__(self)` return a new object (an instance of that class).
- `__init__(self)` is called when the object is initialized.
- `__del__(self)` for del() function. Called when the object is to be destroyed.
- `__repr__(self)` for repr() function. It returns a string to print the object.
- `__str__(self)` for str() function. Return a string to print the object.
- `__bytes__(self)` for bytes() function. Return a byte object which is the byte string representation.
- `__format__(self)` for format() function. Evaluate formatted string literals.

## Comparison Operators

- `__lt__(self, anotherObj)` for < operator.
- `__le__(self, anotherObj)` for <= operator.
- `__eq__(self, anotherObj)` for == operator.
- `__ne__(self, anotherObj)` for != operator.
- `__gt__(self, anotherObj)` for > operator.
- `__ge__(self, anotherObj)` for >= operator.

## Arithmetic Operators

- `__add__(self, anotherObj)` for + operator.
- `__sub__(self, anotherObj)` for – operation on object.
- `__mul__(self, anotherObj)` for * operation on object.
- `__matmul__(self, anotherObj)` for @ operator (numpy matrix multiplication).
- `__truediv__(self, anotherObj)` for simple / division operation on object.
- `__floordiv__(self, anotherObj)` for // floor division operation on object.

## Type Conversion

- `__abs__(self)` make support for abs() function.
- `__int__(self)` support for int() function. Returns the integer value.
- `__float__(self)` for float() function support. Returns float equivalent.
- `__complex__(self)` for complex() function support. Return complex value.
- `__round__(self, nDigits)` for round() function.
- `__trunc__(self)` for trunc() function of math module.
- `__ceil__(self)` for ceil() function of math module.
- `__floor__(self)` for floor() function of math module.

## Emulating Container Types

- `__len__(self)` for len() function. Returns the total number in any container.
- `__getitem__(self, key)` to support index lookup.
- `__setitem__(self, key, value)` to support index assignment
- `__delitem__(self, key)` for del() function. Delete the value at the index.
- `__iter__(self)` returns an iterator when required that iterates all values in the container.

## Summary

Dunder Methods makes our class compatible with inbuilt functions like abs(), len(), str() and many more.
