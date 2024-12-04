#Implement a general program to solve state transfer problems, see details on Kattis.

def get_input():
    num_states, modulus, num_transfers = map(int, input().strip().split())
    state_transfer_matrix = [list(map(int, input().strip().split())) for _ in range(num_states)]
    
    num_start_states = int(input().strip())
    legal_starting_states = list(map(int, input().strip().split()))
    
    num_end_states = int(input().strip())
    legal_ending_states = list(map(int, input().strip().split()))
    
    return num_states, modulus, num_transfers, state_transfer_matrix, legal_starting_states, legal_ending_states


def matrix_multiplication(m1, m2, num_states, modulus):
    # https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm
    # https://www.geeksforgeeks.org/python-program-multiply-two-matrices/
    result = [[0] * num_states for _ in range(num_states)]
    # print(m1)
    for i in range(num_states):
        for j in range(num_states):
            for k in range(num_states):
                result[i][j] = (result[i][j] + m1[i][k] * m2[k][j]) % modulus
    return result

def matrix_exponantiation(m1, power, num_states, modulus):
    # citing some sources here, because i could not for the life of me figure this out on my own
    # https://en.wikipedia.org/wiki/Matrix_exponential 
    # was having a very hard time with this function so i watched  https://www.youtube.com/watch?v=EEb6JP3NXBI and did it based on that kinda?
    # also https://www.geeksforgeeks.org/matrix-exponentiation/ 
    result = [[1 if i == j else 0 for j in range(num_states)] for i in range(num_states)] # identity matrix

    while power:
        if power % 2:
            result = matrix_multiplication(result, m1, num_states, modulus)
        m1 = matrix_multiplication(m1, m1, num_states, modulus)
        power //= 2

    return result



def state_transfer_matrix(legal_starting_states, state_tran_matrix, num_transforms, num_states, modulus, end_states):
    # result_matris = state_tran_matrix
    # for i in range(num_transforms):
    #     result_matris = matrix_multiplication(result_matris, result_matris, num_states, modulus)

    result_matrix = matrix_exponantiation(state_tran_matrix, num_transforms, num_states, modulus)


    total_ways = 0
    for state in legal_starting_states:
        for end in end_states:
            # print("state: ", state)
            # print("end state ", end_states)
            # print("total: ", total_ways)
            total_ways = (total_ways + result_matrix[state][end]) % modulus
    
    print(total_ways % modulus)


def main():
    num_states, modulus, num_transfers, state_tran_matrix, legal_starting_states, legal_ending_states = get_input()
    result = state_transfer_matrix(legal_starting_states, state_tran_matrix, num_transfers, num_states, modulus, legal_ending_states)


    # print(result % modulus)


if __name__ == "__main__":
    main()

# binary exponantiation
# testcase 2
# modulus jafnóðum alls staðar
# k getur verið 0 - þá skila identity matrix

# print((243+525) % 10)