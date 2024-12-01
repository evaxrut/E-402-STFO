# Implement a function that given a prime p such that p = 1 (mod 4) it finds
# an r such that r^2 = −1 (mod p). This is done by first finding a value c such
# that c^(p−1)/2 = −1 (mod p) and letting r = c^(p−1)/4. It can be shown that
# exactly half the non-zero values mod p satisfy this property, so c can be
# chosen randomly until it satisfies this property O(1) expected picks. The
# code written in mAp2 may come in handy here. There can be several correct
# answers, any one of them will be accepted. The input will satisfy p ≤10**18

from B_Binary_Exponentiation import bin_exp
import random


# https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm
number = int(input())

def root_of_min_one(number):
    c_chosen = False
    while not c_chosen:
        c = random.randint(1, number -1)
        c_exp = bin_exp(c, (number - 1) // 2, number)
        if c_exp == number - 1:
            r = bin_exp(c, (number - 1) // 4, number)
            # print(r)
            return r


# # p = 1 mod 4


print(root_of_min_one(number))

# find c(p-1)/2 = -1 (mod p)
# r = c(p-1) / 4


# import math
# print(math.sqrt(-1 % 73))
# print(math.sqrt(6))