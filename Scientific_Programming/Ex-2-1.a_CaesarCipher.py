""""
Exercise 2.1: Caesar Cipher

ToDO:   - exceptions?
        - input function separate?


Author: Oliver Zott
Date: 02.10.2019
"""


def caesar_cipher_encrypt(input, shift):

    sentence_encrypted = ''

    for i in input:
        if i.isupper():
            sentence_encrypted += chr((ord(i) - 65 + shift) % 26 + 65)
        elif i.islower():
            sentence_encrypted += chr((ord(i) - 97 + shift) % 26 + 97)
        else:
            sentence_encrypted += i
    return sentence_encrypted


def caesar_cipher_decrypt(input, shift):

    sentence_decrypted = ''

    for i in input:
        if i.isupper():
            sentence_decrypted += chr((ord(i) - 65 - shift) % 26 + 65)
        elif i.islower():
            sentence_decrypted += chr((ord(i) - 97 - shift) % 26 + 97)
        else:
            sentence_decrypted += i
    return sentence_decrypted


# -------------------------------------------------------
# Test:
encr = caesar_cipher_encrypt("Hallo", 5)
print(encr)
decr = caesar_cipher_decrypt(encr, 5)
print(decr)
test_str1 = "Pbatenghyngvbaf, lbh unir fhpprrqrq va qrpelcgvat gur fgevat"
print(caesar_cipher_decrypt(test_str1, 13))
