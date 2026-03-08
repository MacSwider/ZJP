from foremka import Foremka
from math import sqrt,pi

class ForemkaOkragla(Foremka):
    ksztalt = "okrąg"

    def __init__(self, srednica_mm=50, material="stal"):
        super().__init__(material)   #konstruktor
        self.srednica_mm = srednica_mm

    def pole(self) -> float:
         r = self.srednica_mm / 2
         return pi * r ** 2

    def obwod(self) -> float:
        return pi * self.srednica_mm

    def opis(self) -> str:
        return f"Materiał: {self.material}, Kształt: {self.ksztalt}, Średnica: {self.srednica_mm} mm"
