# Implement code which when given a, b, c, d such that a^2 + b^2 = p and
# c^2 + d^2 = q outputs two solutions to writing pq as a sum of two squares.
# This is best done using the formulas (a^2 + b^2)(c^2 + d^2) = (ac − bd)^2 + (ad + bc)^2
# and (a^2 + b^2)(c^2 + d^2) = (ac + bd)^2 + (ad − bc)^2. This should be printed as
# x^2 + y^2 = pq where x, y and pq are replaced by the corresponding numbers, one
# solution to the formula per line. If x or y are negative, put parentheses
# around them. The input will satisfy a, b, c, d ≤ 10^9.


a, b, c, d = map(int, input().strip().split())

def brahmagupta_fibonacci(a, b, c, d):
    p = a ** 2 + b ** 2
    q = c ** 2 + d ** 2
    # print(p * q)
    outcome = p * q

    x_1 = (a * c - b * d)
    y_1 = (a * d + b * c) 
    x_2 = (a * c + b * d)
    y_2 = (a * d - b * c)

    correct_printing(x_1, y_1, outcome)
    correct_printing(x_2, y_2, outcome)

def correct_printing(x, y, outcome):
    if x < 0 and y < 0:
        print(f"({x})^2 + ({y})^2 = {outcome}")
        return
    if x < 0:
        print(f"({x})^2 + {y}^2 = {outcome}") 
        return
    if y < 0:
        print(f"{x}^2 + ({y})^2 = {outcome}")
        return
    print(f"{x}^2 + {y}^2 = {outcome}") 


brahmagupta_fibonacci(a, b, c, d)