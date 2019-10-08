"""
Implementation of substitute-cipher
"""

import random

'''
print("cipher script: ", __name__)
'''


def cipher(text, method, seed):
    output = ""
    random.seed(seed)

    alphabet = list(r"""!"#$%&'()*+,-./0123456789:;<=>?@ABCD"""
                    r"""EFGHIJKLMNOPQRSTUVWXY Z[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""")

    # need copy, variable assignment wont work cause reference
    alphabet_shuffle = alphabet.copy()
    random.shuffle(alphabet_shuffle)

    if method == 'e':
        dict_cipher = dict(zip(alphabet, alphabet_shuffle))
    elif method == 'd':
        dict_cipher = dict(zip(alphabet_shuffle, alphabet))

    for i in text:
        output += dict_cipher[i]

    return output


'''
if __name__ == "__main__":
    print("cipher is main!")
'''
