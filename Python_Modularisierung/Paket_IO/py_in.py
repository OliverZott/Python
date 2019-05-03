'''
Created on 30.04.2019

@author: Dura
'''

def user_input_int ():
    raw_value = input("Bitte Zahl eingeben: ")
    print("raw_value: ", raw_value)
    int_value = int(raw_value)
    print("Int_Value: ", int_value)
    return int_value

# add text to print
# add argument for text