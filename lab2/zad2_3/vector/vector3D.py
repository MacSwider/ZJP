import math

from .vector2D import Vector2D


class Vector3D(Vector2D):
    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x, y)
        self.z = z

    def length(self) -> float:
        """Długość wektora (norma)."""
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self) -> "Vector3D":
        """Zwraca wektor znormalizowany (jednostkowy)."""
        L = self.length()
        if L == 0:
            raise ValueError("Nie można znormalizować wektora zerowego")
        return Vector3D(self.x / L, self.y / L, self.z / L)

    def dot_product(self, other: "Vector3D") -> float:
        """Iloczyn skalarny z innym wektorem."""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def angle_between(self, other: "Vector3D") -> float:
        """Kąt między tym wektorem a innym (w radianach)."""
        L1 = self.length()
        L2 = other.length()
        if L1 == 0 or L2 == 0:
            raise ValueError("Kąt nie jest określony dla wektora zerowego")
        cos_angle = self.dot_product(other) / (L1 * L2)
        cos_angle = max(-1.0, min(1.0, cos_angle))
        return math.acos(cos_angle)

    # Operatory arytmetyczne
    def __add__(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    # len(Vector3D) — wymiar wektora (liczba składowych)
    def __len__(self) -> int:
        return 3

    # Porównania — wg długości wektora (magnitudy)
    def __gt__(self, other: "Vector3D") -> bool:
        return self.length() > other.length()

    def __lt__(self, other: "Vector3D") -> bool:
        return self.length() < other.length()

    def __ge__(self, other: "Vector3D") -> bool:
        return self.length() >= other.length()

    def __le__(self, other: "Vector3D") -> bool:
        return self.length() <= other.length()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector3D):
            return NotImplemented
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Vector3D):
            return NotImplemented
        return not (self == other)

    # bool(Vector3D) — False dla wektora zerowego
    def __bool__(self) -> bool:
        return self.x != 0 or self.y != 0 or self.z != 0

    # print(Vector3D)
    def __str__(self) -> str:
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def __repr__(self) -> str:
        return f"Vector3D({self.x!r}, {self.y!r}, {self.z!r})"
