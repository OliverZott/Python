'''
Class with Inheritance

Created on 08.05.2019

@author: Oliver Zott
'''

#----------------------------------------------------------------------------------------------------------------

# Base class for money-administration (purse, safe, ...)
class VerwalteterGeldbetrag:
    

    def __init__(self, anfangsbetrag):                          # Constructor of base-class
        self.Betrag = anfangsbetrag
    
    
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
        print("Betrag: {wert:.2f}".format(wert=self.Betrag))    # .2f = float with 2 digits



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
        print("Kundendaten: ", self.Kundendaten)
        VerwalteterGeldbetrag.zeige(self)