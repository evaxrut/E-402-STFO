
from A_State_Transfer_Matrix import state_transfer_matrix

number = int(input())

def build_chess_matrix():
    chess_board = [[0] * 64 for _ in range(64)]

    for i in range(64):
        x = i // 8
        y = i % 8

        directions = [(0, 1), (1, 1), (0, -1), (1, -1), (1, 0), (-1, 1), (-1, 0), (-1, -1)]

        for dx, dy in directions:
            # if x + dx < 0 or x + dx >= 7:
            #     continue # out of bounds
            if not (0 <= x + dx < 8 and 0 <= y + dy < 8):
                continue
            j = 8 * (x + dx) + y + dy
            # print(j)
            # if j < 64:
            chess_board[i][j] = 1
        
    # i = 0
    # for board in chess_board[:15]:
    #     print(i, board[:15])
    return chess_board

def royal_routing(number):
    chess_board = build_chess_matrix()
    legal_start_states = [0]
    legal_end_state = [63]

    transformations = number

    modulo = (10 ** 9 + 7)

    state_transfer_matrix(legal_start_states, chess_board, transformations, 64, modulo, legal_end_state)


royal_routing(number)