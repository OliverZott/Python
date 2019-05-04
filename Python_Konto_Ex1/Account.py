'''
Created on 03.05.2019

@author: Oliver Zott
'''

class Konto:
    '''
    classdocs
    '''
    
    def __init__(self,  inhaber, kontonummer, kontostand, maxTagesumsatz=1500):
        '''
        Constructor
        '''
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self.kontostand = kontostand
        self.maxTagesumsatz = maxTagesumsatz
        self.umsatzHeute = 0
        
    
    def zeige(self):
        #print("Konto von:", self.inhaber)
        print("Konto von {}".format(self.inhaber)) 
        #print("Aktueller Kontostand von Kontonummer {} ist {}: ".format(konto["Kontonummer"],konto["Kontostand"]))
        print("Aktueller Kontostand von Kontonummer {} ist {}: ".format(self.kontonummer,self.kontostand))
        #print("Heute schon {:.2f} von maximal {} umgesetzt".format(konto["UmsatzHeute"], konto["MaxTagesumsatz"]))
        return 
    
    def einzahlen(self, betrag):
        if betrag < 0 or self.umsatzHeute + betrag > self.maxTagesumsatz:
            print("Max Tagesumsatz ueberschritten. Aktueller Tagesumsatz betraegt {}".format(self.umsatzHeute))
            return False
        else:
            self.umsatzHeute += betrag
            self.kontostand += betrag
            return True
        
    def auszahlen(self, betrag):
        if betrag < 0 or self.umsatzHeute + betrag > self.maxTagesumsatz:
            return False
        else:
            self.umsatzHeute += betrag
            self.kontostand -= betrag
            return True
    
    def geldtransfer (self, ziel, betrag):
        if (betrag < 0 or 
            self.umsatzHeute + betrag > self.maxTagesumsatz or 
            ziel.umsatzHeute + betrag > ziel.maxTagesumsatz):
            return False
        else:
            print("Ueberweise {} von Konto {} auf Konto {}".format(betrag,self.kontonummer,ziel.kontonummer))
            self.umsatzHeute += betrag
            ziel.umsatzHeute += betrag
            self.kontostand -= betrag
            ziel.kontostand += betrag
            return True

            
        
    
            