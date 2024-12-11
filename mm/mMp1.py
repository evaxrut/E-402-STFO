# mMp1, 10 points
# In the Ising model our state will be an m x m grid of values ±1, and at the start we have to pick a temperature β to simulate. When we update
# our grid according to our Markov chain we do the following. We pick a random cell in our grid, say (x, y). Let k+ be the number of neighbours
# it has which are +1 and k_ the number of neighbours that are −1. We only consider neighbours up, down, left and right and don’t count out of
# bounds neighbours. We then define Q = exp(2β(k+ − k_)) and finally P = Q / (Q + 1). Finally, with probability P we set the value at (x, y) to 1
# and otherwise to −1. Make a function that takes in such an m x m grid along with three random values a, b, c in [0,1] and uses that to update the
# state. You can let x = ⌊a * m⌋, y = ⌊b * m⌋ and compare P to c in the final step.
import random
import math
from typing import Tuple


def get_pos_neg_neighbours(grid: list, x: int, y: int) -> Tuple[int, int]:
    """TODO: add docstring"""
    pos = 0
    neg = 0
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    for neighbor in neighbors:
        if 0 <= neighbor[0] < len(grid) <= neighbor[1] < len(grid):
            if grid[x + neighbor[0]][y + neighbor[1]] == -1:
                neg += 1
                continue
            pos += 1
    return pos, neg


def update_ising_state(grid: list, temperture: float, a: float, b: float, c: float) -> list: #TODO: how to typehint double list?
    """TODO: add docstring"""
    m = len(grid)
    x = math.floor(a * m)
    y = math.floor(b * m)

    # print("x, y = ", x, ",", y)

    k_minus, k_plus = get_pos_neg_neighbours(grid, x, y)

    Q = math.exp(2 * temperture * (k_plus - k_minus))
    P = Q / (Q + 1)

    if c < P:
        grid[x][y] = 1
    else:
        grid[x][y] = -1

    return grid


if __name__ == "__main__":
    m = 5
    grid = [[random.choice([-1, 1]) for _ in range(m)] for _ in range(m)]

    temperture = 3

    a = random.uniform(0, 1)
    b = random.uniform(0, 1)
    c = random.uniform(0, 1)

    print("Initial Grid:")
    for row in grid:
        print(row)

    updated_grid = update_ising_state(grid, temperture, a, b, c)

    print("Updated Grid:")
    for row in updated_grid:
        print(row)
