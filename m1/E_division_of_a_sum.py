x = int(input())
# x = 10**15
y, z = x, x + 1

if y % 2 == 0:
    y //= 2
else:
    z //= 2

factors = dict()
for val in [y,z]:
    d = 2
    while d * d <= val:
        if val  % d == 0:
            factors[d] = 0
            while val % d == 0:
                factors[d] += 1
                val //= d
        else:
            d += 1

    if val > 1:
        factors[val] = 1

res = 1
for k, v in factors.items():
    res *= v + 1

print(res)