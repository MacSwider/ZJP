# Moduł sphere
# Funkcje: total_surface_area, volume.

import math


def total_surface_area(r: float) -> float:
    """Pole powierzchni całkowitej kuli o promieniu r (4*pi*r^2)."""
    if r <= 0:
        raise ValueError("Promień musi być dodatni")
    return 4 * math.pi * r * r


def volume(r: float) -> float:
    """Objętość kuli o promieniu r ((4/3)*pi*r^3)."""
    if r <= 0:
        raise ValueError("Promień musi być dodatni")
    return (4 / 3) * math.pi * r ** 3


def console_interface():
    # Interfejs z pomocą terminala Pycharma
    print("\n--- Kula ---")
    try:
        r = float(input("Podaj promień r: "))
        print(f"Pole powierzchni całkowitej: {total_surface_area(r):.4f}")
        print(f"Objętość: {volume(r):.4f}")
    except ValueError as e:
        print(f"Błąd: {e}")


if __name__ == "__main__":
    console_interface()
