import VerwalteterGeldbetrag

print('----- Parent-class: -----')
konto1 = VerwalteterGeldbetrag.VerwalteterGeldbetrag(100)
konto1.zeige()
print()

print('----- child-class 1: -----')
konto2 = VerwalteterGeldbetrag.AllgemeinesKonto('Per1', 1000)
konto2.zeige2()
print()

print('----- child-class 2: -----')
konto2 = VerwalteterGeldbetrag.AllgemeinesKontoMitTagesumsatz('Per2', 2000, 400)
konto2.zeige2()
print()

print('----- child-class 3: -----')
konto2 = VerwalteterGeldbetrag.GirokontoMitTagesumsatz('Per3', 1234567, 3000, 500)
konto2.zeige()
print()

print('----- test - programm: -----')
nk1 = VerwalteterGeldbetrag.Nummernkonto(214153646, 13000)
nk2 = VerwalteterGeldbetrag.NummernkontoMitTagesumsatz(347433526, 300, 500)

nk1.einzahlen(45)
nk1.zeige()

nk2.geldtransfer(nk1,450)

nk1.zeige()
nk2.zeige()