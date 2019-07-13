"""
Created on 04.06.2019

@author: Dura
"""

import VerwalteterGeldbetrag

# ----------------------------------------------------------------------------------------------------------------
print("Super-Class 'VerwalteterGeldbetrag'")
print("-------------------------------------------------------------------------------")

konto1 = VerwalteterGeldbetrag.VerwalteterGeldbetrag(1000)
konto1.zeige()

konto1.einzahlen(140)
konto1.zeige()

konto1.einzahlen(-20)
konto1.zeige()

# Testing Getter / Setter
konto1.X = 1111
print(konto1.X)


# ----------------------------------------------------------------------------------------------------------------
# child class
# from VerwalteterGeldbetrag import AllgemeinesKonto
print()
print("sub-class 'AllgemeinesKonto' from Super-Class 'VerwalteterGeldbetrag'")
print("-------------------------------------------------------------------------------")

konto2 = VerwalteterGeldbetrag.AllgemeinesKonto("Olli", 3000)
konto3 = VerwalteterGeldbetrag.AllgemeinesKonto("Leni", 4000)

konto2.zeige_ak()
konto3.zeige_ak()

print()
print()
print("sub-class 'AllgemeinesKontoMitTagesumsatz' from Super-Class 'AllgemeinesKonto'")
print("-------------------------------------------------------------------------------")
# ----------------------------------------------------------------------------------------------------------------
# child class 

konto4 = VerwalteterGeldbetrag.AllgemeinesKontoMitTagesumsatz("TagesOlli", 2000, 400)
konto5 = VerwalteterGeldbetrag.AllgemeinesKontoMitTagesumsatz("Tagesleni", 3000, 400)

konto4.einzahlen(250)
konto3.geldtransfer(konto5, 137)

konto4.zeige_akmt()
konto5.zeige_akmt()

ausz = 57
konto5.auszahlen(ausz)

print("")
print("Tagesleni zahlt aus:", end="")
print(" {arg:.2f}".format(arg=ausz))
print(konto5.Betrag)
# print("Tagesleni hat noch: {val:1f}".format(val=VerwalteterGeldbetrag.AllgemeinesKontoMitTagesumsatz))


# ----------------------------------------------------------------------------------------------------------------
# GiurokontoMitTagesumsatz
print()
print()
print("sub-class 'GirokontoMitTagesumsatz' from Super-Class 'AllgemeinesKontoMitTagesumsatz'")
print("-------------------------------------------------------------------------------")
konto7 = VerwalteterGeldbetrag.GirokontoMitTagesumsatz('Ollgurx', 2253463, 1250, 400)
konto8 = VerwalteterGeldbetrag.GirokontoMitTagesumsatz('Lengurx', '12315632', 1000000, 400)

konto7.zeige()
konto8.zeige()


# ----------------------------------------------------------------------------------------------------------------
# Static Method call
print()
print("Static Method as alternative constructor")
print("-------------------------------------------------------------------------------")

J = VerwalteterGeldbetrag.GirokontoMitTagesumsatz.JuniorKonto("Emil", 124523, 191)
J.zeige()

print()
J.geldtransfer(konto8, 18)
J.zeige()
konto8.zeige()

print()
J.geldtransfer(konto8, 34)
J.zeige()
konto8.zeige()
