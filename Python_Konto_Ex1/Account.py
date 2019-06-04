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
        self.Inhaber = inhaber
        self.Kontonummer = kontonummer
        self.Kontostand = kontostand
        self.MaxTagesumsatz = maxTagesumsatz
        self.UmsatzHeute = 0
        
    
    def zeige(self):
        #print("Konto von:", self.inhaber)
        print("Konto von {}".format(self.Inhaber)) 
        #print("Aktueller Kontostand von Kontonummer {} ist {}: ".format(konto["Kontonummer"],konto["Kontostand"]))
        print("Aktueller Kontostand von Kontonummer {} ist {}: ".format(self.Kontonummer,self.Kontostand))
        #print("Heute schon {:.2f} von maximal {} umgesetzt".format(konto["UmsatzHeute"], konto["MaxTagesumsatz"]))
        return 
    
    def einzahlen(self, betrag):
        if betrag < 0 or self.UmsatzHeute + betrag > self.MaxTagesumsatz:
            print("Max Tagesumsatz ueberschritten. Aktueller Tagesumsatz betraegt {}".format(self.UmsatzHeute))
            return False
        else:
            self.UmsatzHeute += betrag
            self.Kontostand += betrag
            return True
        
    def auszahlen(self, betrag):
        if betrag < 0 or self.UmsatzHeute + betrag > self.MaxTagesumsatz:
            return False
        else:
            self.UmsatzHeute += betrag
            self.Kontostand -= betrag
            return True
    
    def geldtransfer (self, ziel, betrag):
        if (betrag < 0 or 
            self.UmsatzHeute + betrag > self.MaxTagesumsatz or 
            ziel.UmsatzHeute + betrag > ziel.MaxTagesumsatz):
            return False
        else:
            print("Ueberweise {} von Konto {} auf Konto {}".format(betrag,self.Kontonummer,ziel.Kontonummer))
            self.UmsatzHeute += betrag
            ziel.UmsatzHeute += betrag
            self.Kontostand -= betrag
            ziel.Kontostand += betrag
            return True

            
        
    
            