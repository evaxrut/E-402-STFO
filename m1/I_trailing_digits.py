# Find the last 10 digits of 11 + 22 + 33 + ... + n n for an integer n (10 ≤n ≤ 10**7)

number = int(input())
# import time

# def naive_last_ten(number):
#     summ = 0
#     for i in range(1, number):
#         summ += i ** i

#     print(int(str(summ)[-10:]))

def actual_solution(number):
    # start_time = time.time()
    summ = 0
    mod = 10**10
    for i in range(1, number + 1):
        t = pow(i, i, mod)
        summ = (summ + t) % mod

    print(summ)
    # end_time = time.time()
    # print("time: ", end_time - start_time)

# naive_last_ten(number)
actual_solution(number)

