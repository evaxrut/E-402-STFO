# mMp6, 10 points
# Make some code that can plot the results of part 5. 
# Options to do this include matplotlib and seaborn for python. 
# Making a picture where each pixel in the grid is white or black depending on whether the value is +1 or -1 
# is one decent way to plot things. 
# This can also help you see if your algorithm is working correctly, see examples below.

import matplotlib.pyplot as plt
import random

def plot_ising_grid(grid):
    m = len(grid)
    fig, ax = plt.subplots()

    # size = 4000 // (m ** 2)

    for i in range(m):
        for j in range(m):
            color = 'black' if grid[i][j] == 1 else 'white'
            edgecolor = 'black'
            ax.scatter(j, m - i - 1, s=300, c=color, edgecolors=edgecolor)

    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.show()

if __name__ == "__main__":
    grid = [
        [1, -1],
        [-1, 1]
    ]
    m = 15
    # grid = [[random.choice([-1, 1]) for _ in range(m)] for _ in range(m)]
    plot_ising_grid(grid)
