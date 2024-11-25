# Given a positive integer n find the largest prime factor of n (2 ≤n ≤10**9)
import math

number = int(input())

# prime factorization


def largest(number):
    largest = -1
    i = 2

    while number % 2 == 0:
        # 2 is the only even prime num
        largest = 2
        number //= 2

    i += 1
    bound = math.sqrt(number)
    while i <= bound:  # checking sqrt(n)
        while number % i == 0:
            largest = i
            # print(i)
            number //= i
        i += 2
    if number > 2:
        largest = number
    print(largest)


largest(number)
