# Find the number of subsets of a n × k grid of squares that have no two adjacent squares using state transfer matrix.

from A_State_Transfer_Matrix import state_transfer_matrix
# from trash import state_transfer_matrix
# import time

# import cProfile
# import pstats

k, n = map(int, input().strip().split())

def build_matrix(k):

    # start_time = time.time()
    num_states = 2 ** k
    
    states = []
    for i in range(num_states):
        s = bin(i)[2:].zfill(k)
        if '11' not in s:
            states.append(s)

    matrix = [[0] * len(states) for _ in range(len(states))]
    
    for i, s1 in enumerate(states):
        for j, s2 in enumerate(states):
            valid = True
            for x in range(k):
                if s1[x] == '1' and s2[x] == '1':
                    valid = False
                    break
            if valid:
                matrix[i][j] = 1 

    # end_time = time.time()
    # print("Time building matrix:", end_time - start_time)
    return matrix


# def build_matrix(k):
#     start_time = time.time()
#     num_states = 2 ** k

#     states = []
#     for i in range(num_states):
#         s1 = bin(i)[2:].zfill(k)

#         if '11' in s1:
#             continue

#         states.append(s1)

#     matrix = [[0] * len(states) for _ in range(len(states))]
#     for state in range(len(states)):
#         s2 = bin(j)[2:].zfill(k)

#         if '11' in s2:
#             continue

#         valid = True
#         for x in range(k):
#             if s1[x] == '1' and s2[x] == '1':
#                 valid = False
#                 break

#         if valid:
#             matrix[i][j] = 1

#     end_time = time.time()
#     print("time building matrix: ", end_time - start_time)
#     # print("done building matrix")
#     return matrix


def wider_digbuild(k, n):
    matrix = build_matrix(k)

    # print("done building matrix")
    # for row in matrix:
    #     print(row)

    start_states = [0]

    end_states = [x for x in range(len(matrix))]

    # modulus = 10 ** 9 + 7
    # num_states = 2 ** k

    # start_time = time.time()
    # print("matrix size", len(matrix))
    state_transfer_matrix(start_states, matrix, n, len(matrix), end_states)
    # end_time = time.time()
    # print("time: ",  end_time - start_time)

if __name__ == "__main__":  
    # # goal 1000000000000000000
    # cProfile.run("wider_digbuild(10, 1000000000000000000)", "output.prof")
    # # cProfile.run("wider_digbuild(3, 5)", "output.prof")
    # stats = pstats.Stats("output.prof")
    # stats.sort_stats("cumulative").print_stats()
    digbuild = wider_digbuild(k, n)
