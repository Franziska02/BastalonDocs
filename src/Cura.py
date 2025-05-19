from abc import ABC

class Cura():
    def __init__(self, Utilizzi: int, NumeroCure: int, CuraEffettiva: int):

        self.Utilizzi = Utilizzi
        self.NumeroCure = NumeroCure
        self.CuraEffettiva = CuraEffettiva

    def GetStat(self, Utilizzi: int, NumeroCure: int, CuraEffettiva: int):
        pass

    def ScalaUtilizzi(self, Utilizzi):
        pass

    def __str__(self):
        return f"Posso curarmi {self.Utilizzi} volte per {self.CuraEffettiva} punti vita"