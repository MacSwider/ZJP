import figure
from figure.rectangle import total_surface_area as rect_area, perimeter as rect_perimeter
from figure.triangle import total_surface_area as tri_area, perimeter as tri_perimeter


def test_functions():
    """Test wywołań funkcji z pakietu figure."""
    print("=" * 60)
    print("TEST WYWOŁAŃ FUNKCJI (figure)")
    print("=" * 60)

    print("\n--- Prostokąt a=4, b=5 ---")
    print(f"  total_surface_area = {rect_area(4.0, 5.0):.4f}")
    print(f"  perimeter = {rect_perimeter(4.0, 5.0):.4f}")

    print("\n--- Trójkąt 3, 4, 5 ---")
    print(f"  total_surface_area = {tri_area(3.0, 4.0, 5.0):.4f}")
    print(f"  perimeter = {tri_perimeter(3.0, 4.0, 5.0):.4f}")


def check_documentation():
    """Sprawdzenie __name__, __doc__ oraz help() dla funkcji figure."""
    print("\n" + "=" * 60)
    print("SPRAWDZENIE DOKUMENTACJI (__name__, __doc__, help)")
    print("=" * 60)

    funcs = [
        (rect_area, "figure.rectangle.total_surface_area"),
        (rect_perimeter, "figure.rectangle.perimeter"),
        (tri_area, "figure.triangle.total_surface_area"),
        (tri_perimeter, "figure.triangle.perimeter"),
    ]
    for func, label in funcs:
        print(f"\n--- {label} ---")
        print(f"  __name__: {func.__name__}")
        print(f"  __doc__:  {func.__doc__!r}")
        print("  help():")
        help(func)


def check_file_paths():
    """Sprawdzenie __file__ dla pakietu figure i modułów (zadanie 5)."""
    print("\n" + "=" * 60)
    print("SPRAWDZENIE ŚCIEŻEK (__file__)")
    print("=" * 60)
    print(f"\nfigure.__file__ = {figure.__file__}")
    print(f"figure.rectangle.__file__ = {figure.rectangle.__file__}")
    print(f"figure.triangle.__file__ = {figure.triangle.__file__}")


if __name__ == "__main__":
    test_functions()
    check_documentation()
    check_file_paths()
