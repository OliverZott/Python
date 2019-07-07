'''
Created on 04.06.2019

@author: Dura
'''
# from VerwalteterGeldbetrag import GirokontoMitTagesumsatz


# ----------------------------------------------------------------------------------------------------------------
print("Super-Class 'VerwalteterGeldbetrag'")
print("-------------------------------------------------------------------------------")
# First option to call class-definition
import VerwalteterGeldbetrag

konto1 = VerwalteterGeldbetrag.VerwalteterGeldbetrag(1000)

# second option to call class-definition
# from VerwalteterGeldbetrag import VerwalteterGeldbetrag
# konto2 = VerwalteterGeldbetrag(2000)

konto1.zeige()
# konto2.zeige()

konto1.einzahlen(140)
konto1.zeige()

konto1.einzahlen(-20)
konto1.zeige()

print()
print()
print("sub-class 'AllgemeinesKonto' from Super-Class 'VerwalteterGeldbetrag'")
print("-------------------------------------------------------------------------------")
# ----------------------------------------------------------------------------------------------------------------
# child class 
# from VerwalteterGeldbetrag import AllgemeinesKonto


konto3 = VerwalteterGeldbetrag.AllgemeinesKonto("Olli", 3000)
konto4 = VerwalteterGeldbetrag.AllgemeinesKonto("Leni", 4000)  # why error ???

konto4.zeige()

print()
print()
print("sub-class 'AllgemeinesKontoMitTagesumsatz' from Super-Class 'AllgemeinesKonto'")
print("-------------------------------------------------------------------------------")
# ----------------------------------------------------------------------------------------------------------------
# child class 

konto5 = VerwalteterGeldbetrag.AllgemeinesKontoMitTagesumsatz("TagesOlli", 2000, 400)
konto6 = VerwalteterGeldbetrag.AllgemeinesKontoMitTagesumsatz("Tagesleni", 3000, 400)

konto5.einzahlen(250)
konto5.geldtransfer(konto6, 137)

konto5.zeige()
konto6.zeige()

ausz = 57
konto6.auszahlen(ausz)

print("")
print("Tagesleni zahlt aus:", end="")
print(" {arg:.2f}".format(arg=ausz))
print(konto6.Betrag)  # ATTENTION!!! Attribute has to be of first class to be self.
# print("Tagesleni hat noch: {val:1f}".format(val=VerwalteterGeldbetrag.AllgemeinesKontoMitTagesumsatz))


print()
print()
print("sub-class 'GirokontoMitTagesumsatz' from Super-Class 'AllgemeinesKontoMitTagesumsatz'")
print("-------------------------------------------------------------------------------")
# ----------------------------------------------------------------------------------------------------------------
# GiurokontoMitTagesumsatz

konto7 = VerwalteterGeldbetrag.GirokontoMitTagesumsatz('Ollgurx', 2253463, 1250)
konto8 = VerwalteterGeldbetrag.GirokontoMitTagesumsatz('Lengurx', '12315632', 1000000)

konto7.zeige()
konto8.zeige()
