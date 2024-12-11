# mMp4, 20 points
# We now implement sandwiching and “coupling from the past” at once. 
# The function should take a list of extremal states E to sandwich between, a time parameter K, and a random generator r (part 2). 
# It should then simulate what happens to all the states in the list E if we start at time -K+1 and run for K steps 
# (make sure to copy the extremal states rather than change them, use part 3). 
# If all simulations return the same result, we should return that result; otherwise, we try again after doubling K.

# from mMp1 import update_ising_state
from mMp2 import RandomGenerator # settime and gettime
from mMp3 import simulation
import copy

def sandwich(external_states: list, time: int, r: RandomGenerator, grid: list, temperature: float) -> list: #TODO: finna betra nafn
    """TODO: add docstring"""

    while True:
        start_time = -time + 1
        r.set_time(time)

        results = []
        for state in external_states:
            grid_copy = copy.deepcopy(state)
            results.append(simulation(start_time, time, temperature, grid_copy))
        
        if all(res == results[0] for res in results):
            return results
        results = []

        if not results:
            time *= 2

if __name__ == "__main__":
    E = [[[1, -1, 1], [-1, 1, -1], [1, -1, 1]], 
         [[-1, 1, -1], [1, -1, 1], [-1, 1, -1]]] 
    K = 10
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 
    temperature = 1.0
    r = RandomGenerator() 
    
    result = sandwich(E, K, r, grid, temperature)
    print(result)