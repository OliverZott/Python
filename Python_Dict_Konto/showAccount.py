'''
Created on 30.04.2019

@author: Dura
'''

def zeige (konto):
    print("Konto von {}".format(konto["Inhaber"]))
    print("Aktueller Kontostand von Kontonummer {} ist {}: ".format(konto["Kontonummer"],konto["Kontostand"]))
    print("Heute schon {:.2f} von maximal {} umgesetzt".format(konto["UmsatzHeute"], konto["MaxTagesumsatz"]))
    
    