# implement code that reads two inputs a, b ≤ 1018 and outputs their great-
# est common divisor. Do not use a built-in function to do this. It should
# have time complexity O(log(a + b)), which is achievable using Euclid’s
# algorithm

a, b = input().strip().split()
# import random 

def euclid(a, b):
    remainder = -1
    while remainder != 0:
        #45 = 10 * q + r
        # q = b // a
        if b == 0:
            print(a)
            return

        remainder = a % b

        a = b
        b = remainder
        # print(remainder)
    print(a)

# a = random.randint(10**17 -1, 10**18 -1)
# b = random.randint(10**17, 10**18)
        
euclid(int(a), int(b))