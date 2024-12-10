# Make a program to find a primitive root modulo m.
# https://en.wikipedia.org/wiki/Primitive_root_modulo_n
from math import gcd
from G_big_factoring import factorize


def is_ok(factors):  # from board
    if factors == [] or factors == [2] or factors == [2, 2]:
        return True
    if factors.count(2) > 1:
        return False
    odd = set(p for p in factors if p % 2 == 1)
    return len(odd) == 1


def euler_totient(m):
    factors = factorize(m)
    unique_factors = set(factors)

    result = m
    for p in unique_factors:
        result = result * (p - 1) // p
    return int(result)


def primitive_roots(modulo):
    if modulo == 2:
        print(1)
        return
    phi = euler_totient(modulo)
    factors = factorize(phi)

    m_factors = factorize(modulo)
    ok = is_ok(m_factors)

    if not ok:
        print(-1)
        return

    factors = set(factors)

    for g in range(2, modulo):
        if gcd(g, modulo) != 1:
            continue

        is_primitive = True
        for factor in factors:
            if pow(g, phi // factor, modulo) == 1:
                is_primitive = False
                break

        if is_primitive:
            print(g)
            return
    print(-1)


if __name__ == "__main__":
    modulo = int(input())
    roots = primitive_roots(modulo)
