# mMp3, 10 points
# Now we implement our simulation function. It should take a start time Ts, step number k, 
# initial state x0, instance of the rng struct/class r (from part 2). 
# It’s important we use the same r each time so the coupling (in “coupling from the past”) works, 
# and that we set the starting time in r at the beginning. 
# It should then use the function from part 6 k times, getting the three random numbers it needs from r each time, 
# which advances its internal time. Finally, it should return the state we end up in at the end of this process.

from mMp1 import update_ising_state
from mMp2 import Propp_Wilson
import random

random_number_gen = Propp_Wilson()
def simulation(t: int, k: int, x0: int, grid: list) -> list | None:
    """TODO: add docstring"""
    random_number_gen.set_time(t)
    state = None
    for _ in range(k):
        a, b, c = random_number_gen.get_next()
        state = update_ising_state(grid, x0, a, b, c)
    if state:
        return state

if __name__ == "__main__":
    m = 5
    grid = [[random.choice([-1, 1]) for _ in range(m)] for _ in range(m)]
    simulation(0, 6, 0, grid)