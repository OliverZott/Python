'''
Class with Inheritance

Created on 08.05.2019
last Edit: 01.07.2019

@author: Oliver Zott
'''

#----------------------------------------------------------------------------------------------------------------
# Base class for money-administration (purse, safe, ...)
class VerwalteterGeldbetrag:

    def __init__(self, anfangsbetrag):                          # Constructor of base-class
        self.Betrag = anfangsbetrag                             # Betrag: attribute of class 
    
    
    def einzahlenMoeglich(self, betrag):                        # can be overwritten by child-classes!
        return True
    def auszahlenMoeglich(self, betrag):
        return True
    
    def einzahlen(self, betrag):
        if betrag < 0 or not self.einzahlenMoeglich(betrag):
            return False
        else:
            self.Betrag += betrag
            return True
        
    def auszahlen(self,betrag):
        if betrag < 0 or not self.auszahlenMoeglich(betrag):
            return False
        else:
            self.Betrag -= betrag
            return True
    
    def zeige(self):
        #print("Betrag: {:.4f}".format(self.Betrag))             # .2f = float with 2 digits
        print("Betrag_WTF: {wert:.2f}".format(wert=self.Betrag))    # .2f = float with 2 digits



#----------------------------------------------------------------------------------------------------------------
# Missing: Customer-Data, transfer function, 
class AllgemeinesKonto(VerwalteterGeldbetrag):                  # child class
    
    def __init__(self, kundendaten, kontostand):                # constructor of child class
        super().__init__(kontostand)                            # call from Base-Class and connects Arguments
        self.Kundendaten = kundendaten                          # child-class attribute 
        
        
    def geldtransfer(self, ziel, betrag):
        if self.auszahlenMoeglich(betrag) and ziel.einzahlenMoeglich(betrag):
            self.auszahlen(betrag)
            ziel.einzahlen(betrag)
            return True
        else:
            return False
        
    def zeige(self):                                            # class-methode overwritten
        #self.Kundendaten.zeige()
        print("Kundendaten_WTF: ", self.Kundendaten)
        VerwalteterGeldbetrag.zeige(self)



#----------------------------------------------------------------------------------------------------------------
# Missing: "Tagesumsatz"
class AllgemeinesKontoMitTagesumsatz(AllgemeinesKonto):
    
    def __init__(self, kundendaten, contostand, max_Tagesumsatz):
        super().__init__(kundendaten, contostand)
        self.MaxTagesumsatz = max_Tagesumsatz
        self.UmsatzHeute = 0.0
        
    def transferMoeglich(self, betrag):
        return (self.UmsatzHeute + betrag <= self.MaxTagesumsatz)   # condition: returns True or False   
    
    def einzahlenMoeglich(self, betrag):
        return self.transferMoeglich(betrag) 
    
    def auszahlenMoeglich(self, betrag):
        return self.transferMoeglich(betrag)
    
    def einzahlen(self, betrag):
        if AllgemeinesKonto.einzahlen(self, betrag):                # also possible: VerwalteterGeldbetrag.einzahlen(...)
            self.UmsatzHeute += betrag                              # ? Already in parent class, why calculate new here???
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
        AllgemeinesKonto.zeige(self)                                # calls "zeige" from parent classes
        print("Umsatz Heute_WTF:", self.UmsatzHeute)                    # adds new print function to parent "zeiger" stuff
        
        
        
        
        
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
# Missing: Verwaltung der Kundendaten
class GirokontoKundendaten:
    
    def __init__(self,inhaber,kontonummer):
        self.Inhaber = inhaber
        self.Kontonummer = kontonummer    
           
    def zeige(self):
        print("Inhaber:", self.Inhaber)
        print("Kontonummer:",self.Kontonummer)



#----------------------------------------------------------------------------------------------------------------
# Missing: Girokonto
class GirokontoMitTagesumsatz(AllgemeinesKontoMitTagesumsatz):
    
    def __init__(self, inhaber, kontonummer, kontostand, max_tagesumsatz=400):
        kundendaten = GirokontoKundendaten(inhaber, kontonummer)                    
        super().__init__(kundendaten, kontostand, max_tagesumsatz)
        

'''    # so funzt es !!!
class GirokontoMitTagesumsatz(AllgemeinesKontoMitTagesumsatz):
    def __init__(self, inhaber, kontonummer, kontostand, max_tagesumsatz=400):
        kundendaten = GirokontoKundendaten(inhaber, kontonummer)                    
        super().__init__(kundendaten, kontostand, max_tagesumsatz)
        self.Inhaber = inhaber
        self.Kontonummer = kontonummer  
    def zeige(self):
        print("Inhaber:", self.Inhaber)
        print("Kontonummer:",self.Kontonummer)
'''




                    