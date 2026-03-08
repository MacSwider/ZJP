"""
Klasa BigInt — przechowuje liczbę całkowitą jako string.
Operatory arytmetyczne (bez przypisania) zwracają nowy obiekt BigInt.
"""


class BigInt:
    def __init__(self, value: str | int) -> None:
        if isinstance(value, int):
            self._s = str(value)
        else:
            self._s = str(value).strip()
        if not self._s:
            raise ValueError("BigInt wymaga niepustego stringa lub liczby")
        if self._s == "-":
            raise ValueError("Nieprawidłowa wartość BigInt: '-'")
        if self._s[0] == "-":
            if not self._s[1:] or not self._s[1:].isdigit():
                raise ValueError(f"Nieprawidłowa wartość BigInt: {value!r}")
        else:
            if not self._s.isdigit():
                raise ValueError(f"Nieprawidłowa wartość BigInt: {value!r}")

    @property
    def value(self) -> str:
        """Wartość przechowywana jako string."""
        return self._s

    def _to_int(self) -> int:
        return int(self._s)

    @classmethod
    def _from_int(cls, n: int) -> "BigInt":
        return cls(str(n))

    def __add__(self, other: "BigInt") -> "BigInt":
        return self._from_int(self._to_int() + other._to_int())

    def __iadd__(self, other: "BigInt") -> "BigInt":
        self._s = str(self._to_int() + other._to_int())
        return self

    def __sub__(self, other: "BigInt") -> "BigInt":
        return self._from_int(self._to_int() - other._to_int())

    def __isub__(self, other: "BigInt") -> "BigInt":
        self._s = str(self._to_int() - other._to_int())
        return self

    def __mul__(self, other: "BigInt") -> "BigInt":
        return self._from_int(self._to_int() * other._to_int())

    def __imul__(self, other: "BigInt") -> "BigInt":
        self._s = str(self._to_int() * other._to_int())
        return self

    def __gt__(self, other: "BigInt") -> bool:
        return self._to_int() > other._to_int()

    def __lt__(self, other: "BigInt") -> bool:
        return self._to_int() < other._to_int()

    def __ge__(self, other: "BigInt") -> bool:
        return self._to_int() >= other._to_int()

    def __le__(self, other: "BigInt") -> bool:
        return self._to_int() <= other._to_int()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BigInt):
            return NotImplemented
        return self._s == other._s or self._to_int() == other._to_int()

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, BigInt):
            return NotImplemented
        return not (self == other)

    def __str__(self) -> str:
        return self._s

    def __repr__(self) -> str:
        return f"BigInt({self._s!r})"
