#Given a positive integer n calculate the sum of all positive multiples of 3
#and 5 less than n (n ≤ 1018).

# import time
# import random
number = int(input())

# def naive_approach(number):
#     summ = 0
#     for i in range(number):
#         if i % 3 == 0:
#             summ += i
#             continue
#         if i % 5 == 0:
#             summ += i
            
#     print(summ) 
    
def actual_approach(number):
    """ sum = (count / 2) * (first terrm + last term )"""
    # start_time = time.time()
    count_3 = ((number - 1) // 3) 
    highest_3 = count_3 * 3
    sum_3 = (count_3 * (3 + highest_3)) // 2
    
    count_5 = ((number - 1) // 5) 
    highest_5 = count_5 * 5
    sum_5 = (count_5 * (5 + highest_5)) // 2
    
    # overlap 
    count_15 = ((number - 1) // 15) 
    highest_15 = count_15 * 15
    sum_15 = (count_15 * (15 + highest_15)) // 2 
    
    # end_time = time.time()
    print(sum_3 + sum_5 - sum_15)
    # print(f"Time: {end_time - start_time:.6f} seconds")

# number = random.randint(10**18, 10**19)
# print("number ", number)
# naive_approach(number)
actual_approach(number)