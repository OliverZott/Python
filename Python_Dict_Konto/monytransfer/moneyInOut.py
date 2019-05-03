'''
Created on 30.04.2019

@author: Dura
'''

def einzahlen (konto, betrag):
    #testen ob moeglich
    if betrag < 0 or konto["UmsatzHeute"] + betrag > konto["MaxTagesumsatz"]:
        # einzahlung unmoeglich
        return False
    else:
        konto["Kontostand"] += betrag
        konto["UmsatzHeute"] += betrag
        return True

def auszahlen (konto, betrag):
    #testen ob moeglich
    if betrag < 0 or konto["UmsatzHeute"] + betrag > konto["MaxTagesumsatz"]:
        return False
    else:
        konto["Kontostand"] -= betrag
        konto["MaxTagesumsatz"] += betrag
        return True
    