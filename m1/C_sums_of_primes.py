# Given a positive integer n find the sum of all primes less than n (n ≤10**7)

import math

number = int(input())

# Sieve of Eratosthenes
def sieve_of_eratosthenes(number):
    bool_arr = [True for _ in range(number)]

    for i in range(2, int(math.sqrt(number) + 1)):
        if bool_arr[i] is True:
            j = i ** 2
            while j < number:
                bool_arr[j] = False
                j += i
    return [i for i in range(2, number) if bool_arr[i]]

def prime_sum(number):
    primes = sieve_of_eratosthenes(number)

    print(sum(primes))

prime_sum(number)