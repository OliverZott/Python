'''
Created on 30.04.2019

@author: Dura
'''

def fib_rec(n):
    if n < 0: print("Sequence of positive integer")
    elif n == 0: return 0
    elif n == 1: return 1
    else:
        return fib_rec(n-1)+fib_rec(n-2)
