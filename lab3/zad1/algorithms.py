import time

import time

def time_measure(func):
    running = False

    def wrapper(*args, **kwargs):
        nonlocal running

        if not running:  # tylko pierwsze wywołanie
            running = True
            start = time.perf_counter()

            result = func(*args, **kwargs)

            end = time.perf_counter()
            print(f"{func.__name__}: {end-start:.8f} s")

            running = False
            return result
        else:
            return func(*args, **kwargs)

    return wrapper

@time_measure
def alg1(a, n) -> int:
    if n == 0:
        return 1

    if n % 2 == 0:
        polowa = alg1(a, n//2   )
        return polowa * polowa
    else:
        return a * alg1(a, n - 1)


@time_measure
def alg2(a, n) -> int:
    wynik = 1
    i = 0

    while i < n:
        wynik = wynik * a
        i = i + 1

    return wynik


@time_measure
def alg3(a, n) -> int:
    if n == 0:
        return 1

    return a * alg3(a, n - 1)

if __name__ == "__main__":
    alg1(2, 498)        # >= 499 -> RecursionError: maximum recursion depth exceeded
    alg2(2, 498)
    alg3(2, 498)