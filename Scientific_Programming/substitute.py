"""

Author: Oliver Zott
Date: 08.10.2019
"""


import random


# function for the terminal input of string, seed and method
def input_function():

    input_text = input("Please enter text to encrypt // decrypt.")

    while True:
        try:
            seed = int(input("Please enter seed (integer value)."))
        except ValueError as e:
            print("Error... pleas enter integer vale. {}".format(e))
            continue
        break

    method = input("Please press 'e' for encrypt or 'd' for decrypt.")
    while method != 'd' and method != 'e':
        print("Error... only 'e' and 'd' allowed")
        method = input("Please press 'e' for encrypt or 'd' for decrypt.")

    return input_text, method, seed


# function for encrypting / decrypting with given parameters from input_function
def cipher(text, method, seed):

    output = ""

    alphabet = list(r"""!"#$%&'()*+,-./0123456789:;<=>?@ABCD"""
                        r"""EFGHIJKLMNOPQRSTUVWXY Z[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""")
    alphabet_lower = list('abcdefghijklmnopqrstuvwxyz')
    alphabet_upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    random.seed(seed)

    # need copy, variable assignment wont work cause reference
    alphabet_lower_shuffle = alphabet_lower.copy()
    alphabet_upper_shuffle = alphabet_upper.copy()
    alphabet_shuffle = alphabet.copy()

    random.shuffle(alphabet_shuffle)
    random.shuffle(alphabet_lower_shuffle)
    random.shuffle(alphabet_upper_shuffle)

    if method == 'e':
        dict_cipher = dict(zip(alphabet, alphabet_shuffle))
        dict_cipher_lower = dict(zip(alphabet_lower, alphabet_lower_shuffle))
        dict_cipher_upper = dict(zip(alphabet_upper, alphabet_upper_shuffle))
    elif method == 'd':
        dict_cipher = dict(zip(alphabet_shuffle, alphabet))
        dict_cipher_lower = dict(zip(alphabet_lower_shuffle, alphabet_lower))
        dict_cipher_upper = dict(zip(alphabet_upper_shuffle, alphabet_upper))

    for i in text:
        output += dict_cipher[i]

        '''
        if i.isupper():
            output += dict_cipher_upper[i]
        elif i.islower():
            output += dict_cipher_lower[i]
        else:
            output += i
        '''

    print(output)


# main to test implementation
def main():

    text, method, seed = input_function()
    cipher(text, method, seed)


# just checks if file is called from another file or executed directly
if __name__ == "__main__":
    main()
