# Find which starting number under a given positive integer n produces the
# longest Collatz chain. This means we start at n and when we are at an
# even value we divide it by two, and for odd values we multiply it by 3 and
# add 1. Each of these procedures are 1 step. We consider the chains to end at 1 (n ≤10**6)

number = int(input())

def collats_sequenece(number, previously_counted):
    count = 1
    original_number = number
    while number > 1:
        if number in previously_counted:
            count += previously_counted[number]
            break
        # print(number)
        count += 1
        if number % 2 == 0:
            number = number // 2
        else:
            number = (3 * number) + 1
    previously_counted[original_number] = count
    return count


def longest(number):
    lengths = dict()
    max_length = 0
    max_len_num = 0
    for i in range(1, number):
        length = collats_sequenece(i, lengths)
        if length > max_length:
            max_length = length
            max_len_num = i

    print(max_len_num)


longest(number)