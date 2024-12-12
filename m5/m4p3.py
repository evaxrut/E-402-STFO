# m4p3
# Write code that given a set U and a list S of subsets of U uses integer linear programming to find the lowest number of subsets from S that can be used to cover U. U has at most 20 elements. The first line of input contains a single integer n, the size of U. We will consider U to contain the elements 1, 2, ..., n. The next line contains a single integer s ≤ 50, the  number of subsets. The next 2s lines describe the subsets, each 2 lines giving one subset. The first line contains a single integer x, the number of elements in the subset. The second line has x integers, the elements of the subset.


import pulp


def min_subset(size_u: int, subsets: list) -> None:
    p = pulp.LpProblem("Example", pulp.LpMinimize)

    v = pulp.LpVariable.dict("x", range(len(subsets)), cat="Binary")

    # objective
    p += pulp.lpSum(v[i] for i in range(len(subsets)))

    # subject to
    for element in range(1, size_u + 1):
        subset_sum = pulp.lpSum(
            v[j] for j in range(len(subsets)) if element in subsets[j]
        )
        p += subset_sum >= 1

    p.solve(pulp.PULP_CBC_CMD(msg=False))
    selected_subsets = [j for j in range(len(subsets)) if v[j].varValue == 1]
    print(len(selected_subsets))


if __name__ == "__main__":
    size_u = int(input())
    size_s = int(input())

    subsets = []
    for i in range(0, 2 * size_s, 2):
        input()
        subset = list(map(int, input().strip().split()))
        subsets.append(subset)

    min_subset(size_u, subsets)
