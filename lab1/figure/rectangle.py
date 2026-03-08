import math

def total_surface_area(a: float, b: float) -> float:

    if a <= 0 or b <= 0 :
        raise ValueError("Boki muszą być dodatnie")

    s= a*b
    return s

def perimeter(a: float, b: float) -> float:
    if a <= 0 or b <= 0 :
        raise ValueError("Boki muszą być dodatnie")

    return 2*a+2*b

if __name__ == "__main__":
    # Testy modułu triangle
    print("=== Testy modułu rectangle ===")
    a, b = 4.0, 5.0
    print(f"Boki: {a}, {b}")
    print(f"Pole (total_surface_area): {total_surface_area(a, b):.4f}")
    print(f"Obwód (perimeter): {perimeter(a, b):.4f}")
