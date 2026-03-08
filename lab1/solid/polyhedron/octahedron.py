#Moduł octahedron
#Funkcje: total_surface_area, volume.

import math


def total_surface_area(a: float) -> float:
    """Pole powierzchni całkowitej ośmiościanu foremnego o krawędzi a (2*sqrt(3)*a^2)."""
    if a <= 0:
        raise ValueError("Krawędź musi być dodatnia")
    return 2 * math.sqrt(3) * a * a


def volume(a: float) -> float:
    """Objętość ośmiościanu foremnego o krawędzi a (sqrt(2)/3 * a^3)."""
    if a <= 0:
        raise ValueError("Krawędź musi być dodatnia")
    return (math.sqrt(2) / 3) * (a ** 3)


def console_interface():
    # Interfejs z pomocą terminala Pycharma
    print("\n--- Ośmiościan foremny ---")
    try:
        a = float(input("Podaj długość krawędzi a: "))
        print(f"Pole powierzchni całkowitej: {total_surface_area(a):.4f}")
        print(f"Objętość: {volume(a):.4f}")
    except ValueError as e:
        print(f"Błąd: {e}")


if __name__ == "__main__":
    console_interface()
