# mMp6, 10 points
# Make some code that can plot the results of part 5. Options to do this include matplotlib and seaborn for python.  Making a picture where each pixel in the grid is white or black depending on whether the value is +1 or -1 is one decent way to plot things. This can also help you see if your algorithm is working correctly, see examples below.

import matplotlib.pyplot as plt
from mMp5 import ising_model
import seaborn as sns
# print(sns.__version__)

def plot_ising_grid_matplot(grid: list) -> None:
    """TODO: add docstring"""

    m = len(grid)
    fig, ax = plt.subplots()

    for i in range(m):
        for j in range(m):
            color = 'black' if grid[i][j] == 1 else 'white'
            edgecolor = 'black'
            ax.scatter(j, m - i - 1, s=300, c=color, edgecolors=edgecolor)

    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.savefig("/Users/evarut/uni/semester_3/E-402-STFO/mm/fig.jpg")


def plot_ising_grid_seaborn(grid: list) -> None:
    sns.heatmap(grid)
    plt.savefig("/Users/evarut/uni/semester_3/E-402-STFO/mm/fig.jpg")

if __name__ == "__main__":
    m = 30
    grid = ising_model(m, 0.5)
    # for row in grid:
    #     print(row)
    # plot_ising_grid(grid)
    # import os
    # print(os.getcwd())
    plot_ising_grid_seaborn(grid)

