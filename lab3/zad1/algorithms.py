from functools import wraps
from time import perf_counter


def time(arg=1):
    """
    Dekorator pomiaru czasu (zad. 2–4).
    """
    if callable(arg):
        return _time_decorator(1)(arg)
    repeats = arg
    return _time_decorator(repeats)


def _time_decorator(repeats: int):
    def decorator(func):
        running = False

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal running
            if running:
                return func(*args, **kwargs)
            running = True
            try:
                t0 = perf_counter()
                result = None
                for _ in range(repeats):
                    result = func(*args, **kwargs)
                t1 = perf_counter()
                elapsed = t1 - t0
                if repeats == 1:
                    print(f"{func.__name__}: {elapsed:.8f} s")
                else:
                    print(
                        f"{func.__name__}: {elapsed:.8f} s "
                        f"({repeats} wywołań, średnio {elapsed / repeats:.8f} s/wywołanie)"
                    )
                return result
            finally:
                running = False

        return wrapper

    return decorator


@time
def alg1(a, n) -> int:
    if n == 0:
        return 1

    if n % 2 == 0:
        polowa = alg1(a, n // 2)
        return polowa * polowa
    else:
        return a * alg1(a, n - 1)


@time
def alg2(a, n) -> int:
    wynik = 1
    i = 0

    while i < n:
        wynik = wynik * a
        i = i + 1

    return wynik


@time
def alg3(a, n) -> int:
    if n == 0:
        return 1

    return a * alg3(a, n - 1)


if __name__ == "__main__":
    alg1(2, 498)
    alg2(2, 498)
    alg3(2, 498) # >498 z jakiegoś powodu wykrzacza RecursionError: maximum recursion depth exceeded
