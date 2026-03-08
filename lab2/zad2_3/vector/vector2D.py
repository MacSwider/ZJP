import math


class Vector2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def length(self) -> float:
        """Długość wektora."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self) -> "Vector2D":
        """Zwraca wektor znormalizowany (jednostkowy)."""
        L = self.length()
        if L == 0:
            raise ValueError("Nie można znormalizować wektora zerowego")
        return Vector2D(self.x / L, self.y / L)

    def dot_product(self, other: "Vector2D") -> float:
        """Iloczyn skalarny z innym wektorem."""
        return self.x * other.x + self.y * other.y

    def angle_between(self, other: "Vector2D") -> float:
        """Kąt między tym wektorem a innym (w radianach)."""
        L1 = self.length()
        L2 = other.length()
        if L1 == 0 or L2 == 0:
            raise ValueError("Kąt nie jest określony dla wektora zerowego")
        cos_angle = self.dot_product(other) / (L1 * L2)
        cos_angle = max(-1.0, min(1.0, cos_angle))  # ograniczenie ze względu na błędy zaokrągleń
        return math.acos(cos_angle)
