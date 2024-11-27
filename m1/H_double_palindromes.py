# Given a positive integer n print the number of values < n that are palindromes in both base 2 and 10 (n ≤10**12)


# import time

number = int(input())

def base_10_palindromes(n):
    palindromes = []
    # count = 0

    for i in range(10):
        if i >= n:
            break
        # print(i)
        palindromes.append(i)
        # count += 1

    # even
    for i in range(1, 10 ** (len(str(n))) + 1):
        num = str(i) + str(i)[::-1]
        if int(num) >= n:
            break
        if int(num) == int(num[::-1]):
            # print(num)
            palindromes.append(int(num))

        # odd
        for j in range(10):
            num = str(i) + str(j) + str(i)[::-1]
            if int(num) >= n:
                break
            if int(num) == int(num[::-1]):
                palindromes.append(int(num))
                # print(num) 
                # count += 1

    return palindromes

    # print("COUNT: ", count)



def check_base_2_palindrome(number):
    binary = bin(number)[2:]
    # if binary == binary[::-1]:
    #     print("SAME: ", binary, number)
    return binary == binary[::-1]

def also_b_2_pal(number):
    # start_time = time.time()
    b_10_palindromes = set(base_10_palindromes(number))

    double_palindromes = [p for p in b_10_palindromes if check_base_2_palindrome(p)]

    print(len(double_palindromes))

    # end_time = time.time()
    # print("TIME: ", end_time - start_time)

also_b_2_pal(number)
