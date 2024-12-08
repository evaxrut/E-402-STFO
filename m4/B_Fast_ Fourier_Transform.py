#  Implement a polynomial multipication algorithm in O(n log(n)) (by using FFT).
import cmath
import math

# numbers.Complex
# cmath.rect

# https://www.youtube.com/watch?v=h7apO7q16V0&ab_channel=Reducible
# def make_even_deg_polynomial(pol):
#     while not math.log(len(pol), 2).is_integer():
#         pol.append(0)
#     print("even pol: ", pol)
#     return pol


def get_even_odd_pols(pol):
    return pol[::2], pol[1::2]


def fft(p):  # coeff to val
    n = len(p)
    if n == 1:
        return p

    p_even, p_odd = get_even_odd_pols(p)
    f_even = fft(p_even)
    f_odd = fft(p_odd)

    # roots of unity?
    w_n = cmath.rect(1, 2 * cmath.pi / n)

    y = [0] * n
    w = 1
    for i in range(n // 2):
        y[i] = f_even[i] + w * f_odd[i]
        y[i + n // 2] = f_even[i] - w * f_odd[i]
        w *= w_n
    return y


def ifft(p):  # val to coeff
    n = len(p)
    if n == 1:
        return p

    p_even, p_odd = get_even_odd_pols(p)
    f_even = ifft(p_even)
    f_odd = ifft(p_odd)

    # roots of unity?
    w_n = cmath.rect(1, -2 * cmath.pi / n)

    y = [0] * n
    w = 1
    for i in range(n // 2):
        y[i] = f_even[i] + w * f_odd[i]
        y[i + n // 2] = f_even[i] - w * f_odd[i]
        w *= w_n

    return [
        val / 2 for val in y
    ]  # dividing by 2 at every level cus that normalizes it?


def main(pol_1, pol_2, n, m):
    pol_len = 2 ** math.ceil(math.log2(n + m - 1))
    pol_1 = pol_1 + [0] * (pol_len - n)
    pol_2 = pol_2 + [0] * (pol_len - m)

    f1 = fft(pol_1)
    # print(f1)
    f2 = fft(pol_2)
    # print("pols: ", f1, f2)

    result = ifft([f1[i] * f2[i] for i in range(pol_len)])

    # print([round(coeff.real) for coeff in result])
    result = [round(coeff.real) for coeff in result]

    while result and result[-1] == 0:
        result.pop()

    if result:
        print(*result)
    else:
        print(0)


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    pol_1 = list(map(int, input().strip().split()))
    pol_2 = list(map(int, input().strip().split()))
    main(pol_1, pol_2, n, m)
