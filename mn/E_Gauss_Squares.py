# Implement a function which when given a prime p such that p = 1 (mod 4)
# it finds a, b > 0 such that a^2 + b^2 = p. Start by getting the value r from
# the code in mAp3. Then get x, y from the code in mAp4 for the inputs p, r, p.
# Now x^2 + y^2 = p. p will be at most 10^18
from C_Root_of_Minus_One import root_of_min_one
from D_Early_Termination import early_termination
number = int(input())

def gauss_squares(number):
    # get r from mAp3
    r = root_of_min_one(number)
    # get x, y from mAp4
    early_termination(number, r, number)

gauss_squares(number)