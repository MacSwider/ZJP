import solid
from solid.polyhedron import cube, octahedron, tetrahedron
from solid.revolution import cone, cylinder, sphere


def test_functions():
    #Wywołania funkcji total_surface_area i volume z przykładowymi danymi.
    print("=" * 60)
    print("TEST WYWOŁAŃ FUNKCJI")
    print("=" * 60)

    # Sześcian a=2
    a = 2.0
    print(f"\nSześcian (a={a}):")
    print(f"  total_surface_area = {cube.total_surface_area(a):.4f}")
    print(f"  volume = {cube.volume(a):.4f}")

    # Ośmiościan a=2
    print(f"\nOśmiościan (a={a}):")
    print(f"  total_surface_area = {octahedron.total_surface_area(a):.4f}")
    print(f"  volume = {octahedron.volume(a):.4f}")

    # Czworościan a=2
    print(f"\nCzworościan (a={a}):")
    print(f"  total_surface_area = {tetrahedron.total_surface_area(a):.4f}")
    print(f"  volume = {tetrahedron.volume(a):.4f}")

    # Stożek r=1, h=2
    r, h = 1.0, 2.0
    print(f"\nStożek (r={r}, h={h}):")
    print(f"  total_surface_area = {cone.total_surface_area(r, h):.4f}")
    print(f"  volume = {cone.volume(r, h):.4f}")

    # Walec r=1, h=2
    print(f"\nWalec (r={r}, h={h}):")
    print(f"  total_surface_area = {cylinder.total_surface_area(r, h):.4f}")
    print(f"  volume = {cylinder.volume(r, h):.4f}")

    # Kula r=1
    print(f"\nKula (r={r}):")
    print(f"  total_surface_area = {sphere.total_surface_area(r):.4f}")
    print(f"  volume = {sphere.volume(r):.4f}")


def check_documentation():
    """Sprawdzenie __name__, __doc__ oraz help() dla wybranych funkcji."""
    print("\n" + "=" * 60)
    print("SPRAWDZENIE DOKUMENTACJI (__name__, __doc__, help)")
    print("=" * 60)

    funcs = [
        (cube.total_surface_area, "cube.total_surface_area"),
        (cube.volume, "cube.volume"),
        (sphere.total_surface_area, "sphere.total_surface_area"),
        (sphere.volume, "sphere.volume"),
    ]
    for func, label in funcs:
        print(f"\n--- {label} ---")
        print(f"  __name__: {func.__name__}")
        print(f"  __doc__:  {func.__doc__!r}")
        print("  help():")
        help(func)


def check_file_paths():
    """Sprawdzenie __file__ dla pakietu i modułów."""
    print("\n" + "=" * 60)
    print("SPRAWDZENIE ŚCIEŻEK (__file__)")
    print("=" * 60)

    print(f"\nsolid.__file__ = {solid.__file__}")
    print(f"solid.polyhedron.__file__ = {solid.polyhedron.__file__}")
    print(f"solid.revolution.__file__ = {solid.revolution.__file__}")
    print(f"solid.polyhedron.cube.__file__ = {solid.polyhedron.cube.__file__}")
    print(f"solid.polyhedron.octahedron.__file__ = {solid.polyhedron.octahedron.__file__}")
    print(f"solid.polyhedron.tetrahedron.__file__ = {solid.polyhedron.tetrahedron.__file__}")
    print(f"solid.revolution.cone.__file__ = {solid.revolution.cone.__file__}")
    print(f"solid.revolution.cylinder.__file__ = {solid.revolution.cylinder.__file__}")
    print(f"solid.revolution.sphere.__file__ = {solid.revolution.sphere.__file__}")


if __name__ == "__main__":
    test_functions()
    check_documentation()
    check_file_paths()
