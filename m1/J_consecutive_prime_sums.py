
# 41 = 2+3+5+7+11+13 is the longest streak of consecutive primes that
# adds to a prime below a hundred. Which prime below a given positive
# integer n can be written as the sum of the most consecutive primes? (100 ≤ in ≤5 ·106).


# import time
# start_time = time.time()

MAX = 5*10**6 + 100

sieve = [True for _ in range(MAX)]
sieve[0] = sieve[1] = False
for i in range(2, int(MAX**0.5) + 1):
    if sieve[i]:
        for j in range(i * i, MAX, i):
            sieve[j] = False

primes = [i for i in range(2, MAX) if sieve[i]]
number = int(input())

def prime_sum(number):
    prime_set = set(primes)
    prime_sums = [0]

    prime_sums = [0]
    for prime in primes:
        prime_sums.append(prime_sums[-1] + prime)

    max_len = 0
    max_prime = 0

    for i in range(len(prime_sums)):
        for j in range(i - max_len - 1, -1, -1):
            current_sum = prime_sums[i] - prime_sums[j]
            if current_sum >= number:
                break
            if current_sum in prime_set:
                max_len = i - j
                max_prime = current_sum

    print(max_prime)


# number = 5*10**6

prime_sum(number)

# end_time = time.time()

# print("TIME: ", end_time - start_time