""" Unit test for each function in caesar_cypher

Author: Oliver Zott
Date: 2019-11-09
"""

from util import cipher


# Unit test
def test_cipher():
    text = "Dies ist ein Test_t3xt mit symb0len !'%&"
    method = "e"
    seed = 13
    output = cipher.cipher(text, method, seed)

    assert cipher.cipher(output, "d", seed) == text
    assert cipher.cipher(cipher.cipher(text, method, seed), "d", seed) == text
