"""
TODO:   - Add Array to store already calculated values and call if needed
"""

def FirstFactorial(num):
    temp = 1
    while num > 1:
        temp *= num
        num -= 1
    return temp


print(FirstFactorial(int(input("please input number:"))))