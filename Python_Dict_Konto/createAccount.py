'''
Bsp: KONTO 
Buch S.334

Dict / OOP vs Imperativ

Created on 30.04.2019

@author: Dura
'''

def neues_konto(inhaber, kontonummer, kontostand, max_tagesumsatz = 1500):
    return {
        "Inhaber" : inhaber,
        "Kontonummer" : kontonummer,
        "Kontostand" : kontostand,
        "MaxTagesumsatz" : max_tagesumsatz,
        "UmsatzHeute" : 0
        }
