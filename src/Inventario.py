from abc import ABC

class Inventario():
    def __init__(self, Arma1, Arma2, ArmaHolder):

        self.Arma1 = Arma1
        self.Arma2 = Arma2
        self.ArmaHolder = ArmaHolder


    def GetStat(self, Arma1,Arma2):
        pass

    def CambioArma(self, Arma1, Arma2, ArmaHolder):
        pass

    def __str__(self):
        return f"Le mie armi sono {self.Arma1} e {self.Arma2}"