# Given a positive integer n find the prime factors of n (1 < n ≤10**24).
import math

import random

number = int(input())

def is_probable_prime(n): # taken almost straight from lecture + slides
    if n == 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1

    for _ in range(20):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for __ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
            if x == 1:
                return False
        else:
            return False
    return True


def rho(n):
    seed = [2, 3, 5, 7, 11, 13, 1031, 29]
    for s in seed:
        x = s
        y = x
        d = 1
        while d == 1:
            x = (x * x + 1) % n
            y = (y * y + 1) % n
            y = (y * y + 1) % n
            d = math.gcd(abs(x - y), n)
        if d == n:
            continue
        if 1 < d < n:
            return d
    return None


def factorize(number):
    factors = []
    # small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    # for prime in small_primes:
    #     while number % prime == 0:
    #         factors.append(prime)
    #         number //= prime
    if is_probable_prime(number):
        print(number)
        exit(0)
        
    for i in range (2, 1000):
        while number % i == 0:
            factors.append(i)
            number //= i
    todo = [number] #TODO: breyta í queue

    while len(todo) > 0:
        nxt = todo[-1]
        todo.pop()
        if nxt == 1:
            continue
        if is_probable_prime(nxt):
            factors.append(nxt)
            continue
        divisor = rho(nxt)
        todo.append(divisor)
        todo.append(nxt // divisor)
    
    factors.sort()
    # return factors
    print(*factors)


def factoring(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return sorted(factors)


factorize(number)

# for i in range(20):
#     number = random.randint(2, 10)
#     assert (factorize(number) == factoring(number))

# er bara að prenta stærsta