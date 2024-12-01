# Given a, b, k as input use Euclid’s algorithm but stop at 1 ≤ a, b ≤ √k.
# This code will be similar to mAp1 but you have to quit as soon as a, b ≤ √ k.
# The code should return the values a, b. The inputs will satisfy a, b, k ≤ 10**18

# from A_Euclids_Algorithm import euclid
# a, b, k = map(int, input().strip().split())

def early_termination(a, b, k):
    k_sqrt = k ** 0.5
    remainder = -1
    while a > k_sqrt or b > k_sqrt:
        remainder = a % b
        a = b
        b = remainder
        # print(remainder)
    print(max(a, b), min(a, b))

# early_termination(a, b, k)