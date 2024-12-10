# Find all ways to cyclically rotate a vector to make it orthogonal to another vector bu rotating vec 2

# from A_Naive_Convolution import naive_convolution
from B_Fast_Fourier_Transform import fft_main

def make_orth(vec1, vec2, n):
    A = vec2[::-1]+ [0 for _ in range(n)]
    B = vec1[:] + vec1[:] 

    C = fft_main(A, B, n)
    # print("C: ", C)

    if C == 0:
        for i in range(n):
            print(i)
        return

    orth = set()
    for i in range(n -1, (2 * n) - 1):
        if C[i] == 0 and C[i] < n:
            orth.add(i - (n - 1))
    
    if not orth:
        print(-1)
        return
    for o in orth:
        print(o)


if __name__ == "__main__":
    num_cordinates = int(input().strip())
    vec1 = list(map(int, input().strip().split()))
    vec2 = list(map(int, input().strip().split()))
    make_orth(vec1, vec2, num_cordinates)