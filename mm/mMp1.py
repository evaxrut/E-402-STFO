# mMp1, 10 points
# In the Ising model our state will be an m x m grid of values ±1, and at the start we have to pick a temperature β to simulate. When we update our grid according to our Markov chain we do the following. We pick a random cell in our grid, say (x, y). Let k+ be the number of neighbours it has which are +1 and k_ the number of neighbours that are −1. We only consider neighbours up, down, left and right and don’t count out of bounds neighbours. We then define Q = exp(2β(k+ − k_)) and finally P = Q / (Q + 1). Finally, with probability P we set the value at (x, y) to 1 and otherwise to −1. Make a function that takes in such an m x m grid along with three random values a, b, c in [0,1] and uses that to update the state. You can let x = ⌊a * m⌋, y = ⌊b * m⌋ and compare P to c in the final step.
import random
import math
from typing import Tuple
import copy

def get_pos_neg_neighbours(grid: list, x: int, y: int) -> Tuple[int, int]:
    """TODO: add docstring"""
    pos = 0
    neg = 0
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    for nx, ny in neighbors:
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] == 1:
                pos += 1
            elif grid[nx][ny] == -1:
                neg += 1

    return pos, neg


def update_ising_state(grid: list, temperture: float, a: float, b: float, c: float) -> list: #TODO: how to typehint double list?
    """TODO: add docstring"""
    assert all(isinstance(row, list) for row in grid)
    m = len(grid)
    x: int = math.floor(a * m)
    y: int = math.floor(b * m)

    k_plus, k_minus = get_pos_neg_neighbours(grid, x, y)

    Q = math.exp(2 * temperture * (k_minus - k_plus))
    P = Q / (Q + 1)

    if P < c:
        grid[x][y] = 1
    else:
        grid[x][y] = -1

    return grid


if __name__ == "__main__":
    m = 2
    grid = [[random.choice([-1, 1]) for _ in range(m)] for _ in range(m)]
    print(type(grid))

    temperture = 10

    a = random.uniform(0, 1)
    b = random.uniform(0, 1)
    c = random.uniform(0, 1)

    print("Initial Grid:")
    for row in grid:
        print(row)

    updated_grid = update_ising_state(copy.deepcopy(grid), temperture, a, b, c)

    print("Updated Grid:")
    for row in updated_grid:
        print(row)
