'''
Bsp: KONTO 
Buch S.334

Dict / OOP vs Imperativ        -->        Call of Modules

Created on 30.04.2019

@author: Dura
'''
import createAccount                            # call with: 
from showAccount import zeige                   # call with: 

#import monytransfer                             # init for moneyInOut NOT moneytransfers
import monytransfer.monytransfers

k1 = createAccount.neues_konto("Olli", 1234, 1000, 300)
k2 = createAccount.neues_konto("Lena", 5678, 1000000, 100)
zeige(k1)
zeige(k2)

monytransfer.einzahlen(k1, 36.23)
monytransfer.monytransfers.geldtransfer(k1, k2, 36.23)

zeige(k1)
zeige(k2)
