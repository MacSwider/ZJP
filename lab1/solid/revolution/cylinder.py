# Moduł cylinder
# Funkcje: total_surface_area, volume.

import math


def total_surface_area(r: float, h: float) -> float:
    """Pole powierzchni całkowitej walca o promieniu r i wysokości h."""
    if r <= 0 or h <= 0:
        raise ValueError("Promień i wysokość muszą być dodatnie")
    return 2 * math.pi * r * (r + h)


def volume(r: float, h: float) -> float:
    """Objętość walca o promieniu r i wysokości h (pi*r^2*h)."""
    if r <= 0 or h <= 0:
        raise ValueError("Promień i wysokość muszą być dodatnie")
    return math.pi * r * r * h


def console_interface():
    # Interfejs z pomocą terminala Pycharma
    print("\n--- Walec ---")
    try:
        r = float(input("Podaj promień podstawy r: "))
        h = float(input("Podaj wysokość h: "))
        print(f"Pole powierzchni całkowitej: {total_surface_area(r, h):.4f}")
        print(f"Objętość: {volume(r, h):.4f}")
    except ValueError as e:
        print(f"Błąd: {e}")


if __name__ == "__main__":
    console_interface()
