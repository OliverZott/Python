""""
Exercise 02-01 a, b)

Author: Group 1
Date: 10.10.2019
"""


# -------------------------------------------------------
# Exercise 02-01 a)
def caesar_cipher_encrypt(sentence, shift):
    """ Function to encrypt a given sentence. """

    sentence_encrypted = ''

    for i in sentence:
        if i.isupper():
            sentence_encrypted += chr((ord(i) - 65 + shift) % 26 + 65)
        elif i.islower():
            sentence_encrypted += chr((ord(i) - 97 + shift) % 26 + 97)
        else:
            sentence_encrypted += i
    return sentence_encrypted


# -------------------------------------------------------
# Exercise 02-01 b)
def caesar_cipher_decrypt(sentence, shift):
    """ Function to decrypt a given sentence. """

    sentence_decrypted = ''

    for i in sentence:
        if i.isupper():
            sentence_decrypted += chr((ord(i) - 65 - shift) % 26 + 65)
        elif i.islower():
            sentence_decrypted += chr((ord(i) - 97 - shift) % 26 + 97)
        else:
            sentence_decrypted += i
    return sentence_decrypted


# -------------------------------------------------------
# Test:
print(caesar_cipher_encrypt("aBcZ", 1))
print(caesar_cipher_decrypt("Pbatenghyngvbaf, lbh unir fhpprrqrq va qrpelcgvat gur fgevat", 13))



