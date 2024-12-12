# mMp5, 10 points
# We now finally implement the Ising model. The minimum possible result we could get is an m × m grid of all -1, and the maximum possible result we could get is an m × m grid of all +1. Thus, we run the code in the previous part with those states in the list E and the initial time parameter K = 1.

# from mMp3 import
import random 
from mMp2 import RandomGenerator
from mMp4 import sandwich

def ising_model(m: int, temperature: float) -> list:
    time = 1
    random_number_generator = RandomGenerator()
    E = [[random.choice([-1, 1]) for _ in range(m)] for _ in range(m)]
    res = sandwich([E], time, random_number_generator, temperature)
    return res


if __name__ == "__main__":
    m = 4
    beta = 0.0
    result = ising_model(m, beta)
    for row in result:
        print(row)
