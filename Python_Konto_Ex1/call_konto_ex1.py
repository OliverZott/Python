'''
Created on 03.05.2019

@author: Oliver Zott
'''
#import Account                            # Wie Class richtig importieren?
from Account import Konto



print("------------------------------------------")
print("Class name: ", Konto.__name__)
print("Module name in which the class is defined: ", Konto.__module__ )
print("Base classes, in the order of their occurrence in the base class list: ", Konto.__bases__ )
#print("Path: ", Employee.__file__  )   #why no path ???
print("------------------------------------------")


#konto1 = Account.Konto("Olli", 12345, 2000)            
konto1 = Konto("Olli", 12345, 2000)
konto2 = Konto("Zwuuugu", 56789, 10000)
print("Kontostand 'raw': "), konto1.zeige()
print("")

konto1.einzahlen(150)
konto1.einzahlen(1400)
konto1.zeige()
print("")

konto1.geldtransfer(konto2, 1000)
konto1.zeige()
konto2.zeige()