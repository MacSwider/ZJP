import math

def total_surface_area(a: float, b: float, c: float) -> float:
    """Pole trójkąta wzorem Herona. a, b, c – długości boków."""
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Boki muszą być dodatnie")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Nierówność trójkąta nie jest spełniona")
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def perimeter(a: float, b: float, c: float) -> float:
    """Obwód trójkąta o bokach a, b, c."""
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Boki muszą być dodatnie")
    return a + b + c


if __name__ == "__main__":
    # Testy modułu triangle
    print("=== Testy modułu triangle ===")
    # Trójkąt 3, 4, 5 (prostokątny), pole = 6, obwód = 12
    a, b, c = 3.0, 4.0, 5.0
    print(f"Boki: {a}, {b}, {c}")
    print(f"Pole (total_surface_area): {total_surface_area(a, b, c):.4f}")
    print(f"Obwód (perimeter): {perimeter(a, b, c):.4f}")
    print()
    # Trójkąt równoboczny a=2
    a = b = c = 2.0
    print(f"Trójkąt równoboczny a={a}")
    print(f"Pole: {total_surface_area(a, b, c):.4f}")
    print(f"Obwód: {perimeter(a, b, c):.4f}")