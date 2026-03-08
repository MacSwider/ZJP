#Moduł tetrahedron
#Funkcje: total_surface_area, volume.

import math


def total_surface_area(a: float) -> float:
    """Pole powierzchni całkowitej czworościanu foremnego o krawędzi a, P= (sqrt(3)*a^2)."""
    if a <= 0:
        raise ValueError("Krawędź musi być dodatnia")
    return math.sqrt(3) * a * a


def volume(a: float) -> float:
    """Objętość czworościanu foremnego o krawędzi a , V= (a^3 / (6*sqrt(2)))."""
    if a <= 0:
        raise ValueError("Krawędź musi być dodatnia")
    return (a ** 3) / (6 * math.sqrt(2))


def console_interface():
    # Interfejs z pomocą terminala Pycharma
    print("\n--- Czworościan foremny ---")
    try:
        a = float(input("Podaj długość krawędzi a: "))
        print(f"Pole powierzchni całkowitej: {total_surface_area(a):.4f}")
        print(f"Objętość: {volume(a):.4f}")
    except ValueError as e:
        print(f"Błąd: {e}")


if __name__ == "__main__":
    console_interface()
