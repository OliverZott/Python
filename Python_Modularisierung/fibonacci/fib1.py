'''
Created on 30.04.2019

@author: Dura
'''

def fib_1(n):
    fib_list = [0,1]
    a = 0
    b = 1
    for i in range(1, n, 1): 
        #print("a: ", a)
        #print("b: ", b)
        a, b = b, a+b
        #print("a2: ", a)
        #print("b2: ", b)
        fib_list.extend([b])            # to add int to list use []
        #print(fib_list[0])
    print(fib_list)
    return b
