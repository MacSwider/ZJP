# Moduł cube
# Funkcje: total_surface_area, volume.


def total_surface_area(a: float) -> float:
    """Pole powierzchni całkowitej sześcianu o krawędzi a (wzór 6*a^2)."""
    if a <= 0:
        raise ValueError("Krawędź musi być dodatnia")
    return 6 * a * a


def volume(a: float) -> float:
    """Objętość sześcianu o krawędzi a (wzór a^3)."""
    if a <= 0:
        raise ValueError("Krawędź musi być dodatnia")
    return a ** 3


def console_interface():
    # Interfejs z pomocą terminala Pycharma
    print("\n--- Sześcian ---")
    try:
        a = float(input("Podaj długość krawędzi a: "))
        print(f"Pole powierzchni całkowitej: {total_surface_area(a):.4f}")
        print(f"Objętość: {volume(a):.4f}")
    except ValueError as e:
        print(f"Błąd: {e}")


if __name__ == "__main__":
    console_interface()
