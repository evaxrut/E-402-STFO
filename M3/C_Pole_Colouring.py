# Colour lightposts in several colours using state transfer matrix, see details on Kattis.
from A_State_Transfer_Matrix import state_transfer_matrix

number = int(input())

def pole_coloring(number):
    # pole_matrix = [
    #     [2, 2, 1, 2, 1, 2, 1, 2],
    #     [2, 2, 2, 1, 2, 1 ,2, 1],
    #     [1, 2, 2, 2, 1, 2, 1, 2],
    #     [2, 1, 2, 2, 2, 1, 2, 1],
    #     [1, 2, 1, 2, 2, 2, 1, 2],
    #     [2, 1, 2, 1, 2, 2, 2, 1],
    #     [1, 2, 1, 2, 1, 2, 2, 2],
    #     [2, 1, 2, 1, 2, 1, 2, 2]
    # ]
    # return pole_matrix

    pole_matrix = [
        [2, 2, 1, 0, 1, 0, 0, 0], 
        [2, 2, 0, 1, 0, 1, 0, 0], 
        [1, 0, 2, 2, 0, 0, 1, 0], 
        [0, 1, 2, 2, 0, 0, 0, 1], 
        [1, 0, 0, 0, 2, 2, 1, 0], 
        [0, 1, 0, 0, 2, 2, 0, 1], 
        [0, 0, 1, 0, 1, 0, 2, 2], 
        [0, 0, 0, 1, 0, 1, 2, 2]
    ]
    return pole_matrix



pole_matrix = pole_coloring(number)
starting_states = [0]
ending_states =  [2]

state_transfer_matrix(starting_states, pole_matrix, number, 8, 10** 9 + 7, ending_states)