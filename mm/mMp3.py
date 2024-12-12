# mMp3, 10 points
# Now we implement our simulation function. It should take a start time Ts, step number k, initial state x0, instance of the rng struct/class r (from part 2). It’s important we use the same r each time so the coupling (in “coupling from the past”) works, and that we set the starting time in r at the beginning. It should then use the function from part 6 k times, getting the three random numbers it needs from r each time, which advances its internal time. Finally, it should return the state we end up in at the end of this process.

from mMp1 import update_ising_state
from mMp2 import RandomGenerator
import random

def simulation(start_time: int, step_number: int, temperature: float, grid: list, random_number_gen: RandomGenerator) -> list | None:
    """TODO: add docstring"""
    random_number_gen.set_time(start_time)
    state = grid
    for _ in range(step_number):
        a, b, c = random_number_gen.get_next()
        assert all(isinstance(row, list) for row in grid)
        state = update_ising_state(state, temperature, a, b, c)
    if state:
        return state

if __name__ == "__main__":
    m = 2
    grid = [[random.choice([-1, 1]) for _ in range(m)] for _ in range(m)]
    print("original grid")
    for row in grid:
        print(row)

    updated_grid = simulation(0, 6, 0.5, grid, RandomGenerator())
    print("updated grid")
    if updated_grid:
        for row in updated_grid:
            print(row)
