# Implement a polynomial multipication algorithm in O(n^2)

n, m = map(int, input().strip().split())
pol_1 = input().strip().split()
pol_2 = input().strip().split()

def naive_convolution(pol_1, pol_2, n, m):
    product = [0] * (n + m)
    for i in range(n):
        for j in range(m):
            product[i + j] += int(pol_1[i]) * int(pol_2[j])
   
    product =  [i for i in product if i != 0]
    if not product:
        print(0)
        return
    print(*product)

if __name__ == "__main__":
    naive_convolution(pol_1, pol_2, n, m)