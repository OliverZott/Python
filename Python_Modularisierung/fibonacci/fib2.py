'''
Created on 30.04.2019

@author: Dura
'''

def fib_2 ( zahl ):
    a, b = 0, 1
    while zahl > 1:               # range(4) = 0, 1, 2, 3
        a, b = b, a+b
        print(a,b)
        zahl = zahl-1
    return a
