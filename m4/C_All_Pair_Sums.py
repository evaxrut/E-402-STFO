# Find all ways to write a value as the sum of two numbers from a multiset

import math
from B_Fast_Fourier_Transform import fft_main

def calc(multiset_1, multiset_2, n, m):
    min_sum = min(multiset_1) + min(multiset_2)
    max_sum = max(multiset_1) + max(multiset_2)

    fft_size = 2 ** math.ceil(math.log2(max_sum - min_sum + 1))

    zero_idx = -min_sum

    freq_A = [0] * fft_size
    freq_B = [0] * fft_size

    min_1 = min(multiset_1)
    min_2 = min(multiset_2)

    for a in multiset_1:
        freq_A[a - min_1] += 1
    for b in multiset_2:
        freq_B[b - min_2] += 1
    # print("done making freq tables")

    conv = fft_main(freq_A, freq_B, fft_size)
    # print("conv: ", conv)

    conv_counts = [c for c in conv]

    return conv_counts, zero_idx


def num_ways(convolution, x, zero_idx):
    idx = x + zero_idx
    if 0 <= idx < len(convolution):
        print(convolution[idx])
    else:
        print(0)


def main():
    n, m = map(int, input().strip().split())
    multiset_1 = list(map(int, input().strip().split()))
    multiset_2 = list(map(int, input().strip().split()))

    num_queries = int(input())

    convolution, zero_idx = calc(multiset_1, multiset_2, n, m)

    for _ in range(num_queries):
        num_ways(convolution, int(input()), zero_idx)


if __name__ == "__main__":
    main()


# 2 2
# 2 2
# 2 2
# 2
# 2
# 4