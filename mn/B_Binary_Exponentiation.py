# Implement a modular power function, taking as input the base b, exponent
# e and modulus m, outputting be (mod m). Do not use a built-in function
# to do this. It should have time complexity O(log(e)), so binary exponenti-
# ation is needed. The inputs will satisfy b, e, m ≤1018, b, e ≥0 and m > 1.
# We will consider 00 to be 1

# a, e, m = map(int, input().strip().split())

# https://en.wikipedia.org/wiki/Modular_exponentiation
def bin_exp(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result =  (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

# bin_exp(a, e, m)