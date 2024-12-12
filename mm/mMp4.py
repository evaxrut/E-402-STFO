# mMp4, 20 points
# We now implement sandwiching and “coupling from the past” at once. The function should take a list of extremal states E to sandwich between, a time parameter K, and a random generator r (part 2). It should then simulate what happens to all the states in the list E if we start at time -K+1 and run for K steps (make sure to copy the extremal states rather than change them, use part 3). If all simulations return the same result, we should return that result; otherwise, we try again after doubling K.

from mMp2 import RandomGenerator
from mMp3 import simulation
import copy
import random

def sandwich(external_states: list, time: int, r: RandomGenerator, temperature: float) -> list: #TODO: finna betra nafn
    """TODO: add docstring"""

    while True:
        start_time = -time + 1
        r.set_time(time)

        results = []
        for state in external_states:
            grid_copy = copy.deepcopy(state)
            assert all(isinstance(row, list) for row in grid_copy)
            results.append(simulation(start_time, time, temperature, grid_copy, RandomGenerator()))
        
        if all(res == results[0] for res in results):
            # print(results[0])
            return results[0]

        time *= 2

if __name__ == "__main__":
    # E = [[1, -1], [1, -1]], [[1, 1], [-1, -1]]
    m = 2
    E = [[random.choice([-1, 1]) for _ in range(m)] for _ in range(m)]
    K = 10
    temperature = 0
    r = RandomGenerator() 
    
    result = sandwich([E], K, r, temperature)
    print(result)