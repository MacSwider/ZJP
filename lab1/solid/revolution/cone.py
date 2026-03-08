# Moduł cone - stożek.
# Funkcje: total_surface_area, volume.

import math


def total_surface_area(r: float, h: float) -> float:
    """Pole powierzchni całkowitej stożka o promieniu r i wysokości h."""
    if r <= 0 or h <= 0:
        raise ValueError("Promień i wysokość muszą być dodatnie")
    return math.pi * r * (r + math.sqrt(r * r + h * h))


def volume(r: float, h: float) -> float:
    """Objętość stożka o promieniu r i wysokości h ((1/3)*pi*r^2*h)."""
    if r <= 0 or h <= 0:
        raise ValueError("Promień i wysokość muszą być dodatnie")
    return (1 / 3) * math.pi * r * r * h


def console_interface():
    # Interfejs z pomocą terminala Pycharma
    print("\n--- Stożek ---")
    try:
        r = float(input("Podaj promień podstawy r: "))
        h = float(input("Podaj wysokość h: "))
        print(f"Pole powierzchni całkowitej: {total_surface_area(r, h):.4f}")
        print(f"Objętość: {volume(r, h):.4f}")
    except ValueError as e:
        print(f"Błąd: {e}")


if __name__ == "__main__":
    console_interface()
