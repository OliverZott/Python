'''
Created on 30.04.2019

@author: Dura
'''

def geldtransfer (quelle, ziel, betrag):
    # Test ob Transfer möglich
    if (betrag < 0 or 
        quelle["UmsatzHeute"] + betrag > quelle["MaxTagesumsatz"] or
        ziel["UmsatzHeute"] + betrag > ziel["MaxTagesumsatz"]):
        # Transfer nicht moeglich
        return False
    else:
        # transfer moeglich
        quelle["Kontostand"] -= betrag
        quelle["UmsatzHeute"] += betrag
        ziel["Kontostand"] += betrag
        ziel["UmsatzHeute"] += betrag
        return True