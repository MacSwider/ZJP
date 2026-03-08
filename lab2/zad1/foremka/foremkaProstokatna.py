from foremka import Foremka

class ForemkaProstokatna(Foremka):
     ksztalt = "prostokąt"
     a_mm = 40
     b_mm = 60

     def __init__(self, a_mm=40,b_mm=60, material="stal"):
         super().__init__(material)  # konstruktor
         self.a_mm = a_mm
         self.b_mm = b_mm


     def pole(self) -> float:
         return self.a_mm * self.b_mm

     def obwod(self) -> float:
        return 2 * (self.a_mm + self.b_mm)

     def opis(self) -> str:
        return f"Materiał: {self.material}, Kształt: {self.ksztalt}, Wymiary: {self.a_mm}×{self.b_mm} mm"