'''
Created on 04.06.2019

@author: Dura
'''


#----------------------------------------------------------------------------------------------------------------
print("Super-Class 'VerwalteterGeldbetrag'")
print("--------------------------------------------------------------------------------------")
# First option to call class-definition
import VerwalteterGeldbetrag
konto1 = VerwalteterGeldbetrag.VerwalteterGeldbetrag(1000)

# second option to call class-definition
#from VerwalteterGeldbetrag import VerwalteterGeldbetrag
#konto2 = VerwalteterGeldbetrag(2000)

konto1.zeige()
#konto2.zeige()

konto1.einzahlen(140)
konto1.zeige()

konto1.einzahlen(-20)
konto1.zeige()

print()
print()
print("sub-class 'AllgemeinesKonto' from Super-Class 'VerwalteterGeldbetrag'")
print("--------------------------------------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------
# child class 

#konto4 = VerwalteterGeldbetrag.AllgemeinesKonto(("Leni",4000))          # why error ???


from VerwalteterGeldbetrag import AllgemeinesKonto
konto3 = AllgemeinesKonto("Olli",3000)

konto3.zeige()