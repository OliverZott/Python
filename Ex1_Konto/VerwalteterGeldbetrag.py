"""
Class with Inheritance

Date: 01.07.2019
@author: Oliver Zott
"""


# ----------------------------------------------------------------------------------------------------------------
# Parent class for money-administration (purse, safe, ...)

class VerwalteterGeldbetrag:

    def __init__(self, anfangsbetrag):  # Constructor of base-class
        self.Betrag = anfangsbetrag  # Betrag: attribute of class

    def einzahlenMoeglich(self, betrag):  # can be overwritten by child-classes!
        return True

    def auszahlenMoeglich(self, betrag):
        return True

    def einzahlen(self, betrag):
        if betrag < 0 or not self.einzahlenMoeglich(betrag):
            return False
        else:
            self.Betrag += betrag
            return True

    def auszahlen(self, betrag):
        if betrag < 0 or not self.auszahlenMoeglich(betrag):
            return False
        else:
            self.Betrag -= betrag
            return True

    def zeige(self):
        # print("Betrag: {:.4f}".format(self.Betrag))  # .2f = float with 2 digits
        print("Betrag (Parent-Class): {wert:.2f}".format(wert=self.Betrag))  # .2f = float with 2 digits

    def zeige2(self):
        print("Betrag2 (Parent-Class): {wert:.2f}".format(wert=self.Betrag))


# ----------------------------------------------------------------------------------------------------------------
# Cash: Cash-repositories can't have negative money

class VerwalteterBargeldbetrag(VerwalteterGeldbetrag):

    def __init__(self, bargeldbetrag):
        if bargeldbetrag < 0:
            bargeldbetrag = 0

        super().__init__(bargeldbetrag)

    def auszahlenMoeglich(self, betrag):
        return self.Betrag >= betrag


class Geldboerse(VerwalteterBargeldbetrag):

    # TODO: special class for a purse
    pass


class Tresor(VerwalteterBargeldbetrag):
    # TODO: special class for a safe
    pass

# ----------------------------------------------------------------------------------------------------------------
# Missing: Customer-Data, transfer function
class AllgemeinesKonto(VerwalteterGeldbetrag):  # child class

    def __init__(self, kundendaten, kontostand):  # constructor of child class
        super().__init__(kontostand)  # call from Base-Class and connects Arguments
        self.Kundendaten = kundendaten  # child-class attribute

    def geldtransfer(self, ziel, betrag):
        if self.auszahlenMoeglich(betrag) and ziel.einzahlenMoeglich(betrag):
            self.auszahlen(betrag)
            ziel.einzahlen(betrag)
            return True
        else:
            return False

    def zeige(self):
        self.Kundendaten.zeige()  # calls function from class "GirokontoKundendaten"
        # super().zeige()  # same as next line
        VerwalteterGeldbetrag.zeige(self)
        # print("Kundendaten (Child-Class 1): ", self.Kundendaten)

    def zeige2(self):
        super().zeige2()  # same as next line
        print("Kundendaten (Child-Class 1): ", self.Kundendaten)


# ----------------------------------------------------------------------------------------------------------------
# Missing: "Tagesumsatz"

class AllgemeinesKontoMitTagesumsatz(AllgemeinesKonto):

    def __init__(self, kundendaten, kontostand, max_Tagesumsatz):
        super().__init__(kundendaten, kontostand)
        self.MaxTagesumsatz = max_Tagesumsatz
        self.UmsatzHeute = 0.0

    def transferMoeglich(self, betrag):
        return self.UmsatzHeute + betrag <= self.MaxTagesumsatz  # condition: returns True or False

    def einzahlenMoeglich(self, betrag):
        return self.transferMoeglich(betrag)

    def auszahlenMoeglich(self, betrag):
        return self.transferMoeglich(betrag)

    def einzahlen(self, betrag):
        if AllgemeinesKonto.einzahlen(self, betrag):  # also possible: VerwalteterGeldbetrag.einzahlen(...)
            self.UmsatzHeute += betrag  # Already in parent class, why calculate new here?
            return True
        else:
            return False

    def auszahlen(self, betrag):
        if VerwalteterGeldbetrag.auszahlen(self, betrag):
            self.UmsatzHeute -= betrag
            return True
        else:
            return False

    def zeige(self):
        AllgemeinesKonto.zeige(self)  # calls "zeige" from parent classes
        print("Tagesumsatz (Child-Class 2):", self.UmsatzHeute)  # adds new print function

    def zeige2(self):
        AllgemeinesKonto.zeige2(self)
        print("Tagesumsatz (Child-Class 2):", self.UmsatzHeute)


# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# Missing: Verwaltung der Kundendaten

class GirokontoKundendaten:

    def __init__(self, inhaber, kontonummer):
        self.Inhaber = inhaber
        self.Kontonummer = kontonummer

    def zeige(self):
        print("Inhaber:", self.Inhaber)
        print("Kontonummer:", self.Kontonummer)


class NummernkontoKundendaten:

    def __init__(self, identifikationsnummer):
        self.Identifikationsnummer = identifikationsnummer

    def zeige(self):
        print('Identifikationsnummer: ', self.Identifikationsnummer)


# ----------------------------------------------------------------------------------------------------------------
# Missing: Girokonto

class GirokontoMitTagesumsatz(AllgemeinesKontoMitTagesumsatz):

    def __init__(self, inhaber, kontonummer, kontostand, max_tagesumsatz):
        kundendaten = GirokontoKundendaten(inhaber, kontonummer)
        super().__init__(kundendaten, kontostand, max_tagesumsatz)


class Girokonto(AllgemeinesKonto):

    def __iadd__(self, inhaber, kontonummer, kontostand):
        kundendaten = GirokontoKundendaten(inhaber, kontonummer)
        super().__init__(kundendaten, kontostand)


# ----------------------------------------------------------------------------------------------------------------
# Nummernkonto

class Nummernkonto(AllgemeinesKonto):

    def __init__(self, identifikationsnummer, kontostand):
        kundendaten = NummernkontoKundendaten(identifikationsnummer)
        super().__init__(kundendaten,kontostand)


class NummernkontoMitTagesumsatz(AllgemeinesKontoMitTagesumsatz):

    def __init__(self, kontonummer, kontostand, max_tagesumsatz):
        kundendaten = NummernkontoKundendaten(kontonummer)
        super().__init__(kundendaten, kontostand, max_tagesumsatz)
