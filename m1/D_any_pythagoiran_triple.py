# Given a positive integer n find a Pythagorean triple (a, b, c) such that
# a + b + c = n. Separate the output numbers by spaces. A Pythagorean
# triple (a, b, c) is a triple of positive integers such that a2 +b2 = c2. If there
# are multiple answers, choose any one of them. If there is no answer print
# 0 0 0 instead (n ≤104).
# import time
number = int(input())

def make_triple(m, n):
    m2 = m * m
    n2 = n * n
    a = m2 - n2
    b = 2 * m * n
    c = m2 + n2
    if a != 0 and b!= 0 and c!= 0:
        return a, b, c

# def naive_solution(number):
#     for m in range(number):
#         for n in range(m):
#             triple = make_triple(m, n)
#             if triple and sum(triple) == number:
#                 print(triple)
#                 return

# def actual_solution(number):
#     # start_time = time.time()
    
#     for m in range(2,  int(number**0.5) + 1):
#         for n in range(m - 1, 0, -1):
#             if (m - n) % 2 == 1 and gcd(m, n) == 1:  # Ensuring primitive triples
#             #TODO: coprime check
#                 triple = make_triple(m, n)
#                 if triple and sum(triple) == number:
#                     print(*triple)
#                     # end_time = time.time()
#                     # print(f"Time: {end_time - start_time:.6f} seconds")
#                     return

#     print(0, 0, 0)
#     # end_time = time.time()
#     # print(f"Time: {end_time - start_time:.6f} seconds")


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def actual_solution(number):
    for m in range(2, int((number // 2) ** 0.5) + 1):
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                # primitivd triple
                a_0 = m * m - n * n
                b_0 = 2 * m * n
                c_0 = m * m + n * n
                sum0 = a_0 + b_0 + c_0

                k_max = number // sum0
                for k in range(1, k_max + 1):
                    # scaling
                    a = k * a_0
                    b = k * b_0
                    c = k * c_0
                    if a + b + c == number:
                        print(a, b, c)
                        return
    print(0, 0, 0)

actual_solution(number)