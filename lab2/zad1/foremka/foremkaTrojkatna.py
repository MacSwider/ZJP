from foremka import Foremka
from math import sqrt

class ForemkaTrojkatna(Foremka):

    ksztalt = "trójkąt równoboczny"

    def __init__(self, bok_mm=50, material="stal"):
        super().__init__(material)   #konstruktor
        self.bok_mm = bok_mm

    def pole(self) -> float:
        return (self.bok_mm * self.bok_mm * sqrt(3)) / 4

    def obwod(self) -> float:
        return 3 * self.bok_mm

    def opis(self) -> str:
        return f"Materiał: {self.material}, Kształt: {self.ksztalt}, Bok: {self.bok_mm} mm"