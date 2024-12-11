# m4p1
# Write code that given a graph G uses integer linear programming to find the size of the maximum clique. A clique is a subset of vertices where every vertex is connected to every other vertex. The graph is given as follows. The first line contains two integers V, E, the number of vertices and edges. Then E lines follow, each containing two integers a, b, meaning that there is an edge between vertices a and b. These values are 0-indexed and the graph will be simple. The input will satisfy 1 ≤ V ≤ 25.

import pulp


def max_clique_size(graph_dict, num_verticies):
    all_vertices = set(graph_dict)
    p = pulp.LpProblem("Example", pulp.LpMaximize)


    v = pulp.LpVariable.dict("x", range(num_verticies), cat="Binary")

    # objective
    p += pulp.lpSum(v[i] for i in range(num_verticies))

    # subject to
    for i in range(num_verticies):
        connected_to = set(graph_dict.get(i, []))
        not_connected = all_vertices.difference(connected_to) - {i}
        for j in not_connected:
            p += v[i] + v[j] <= 1

    p.solve(pulp.PULP_CBC_CMD(msg = False))

    clique_size = sum(v[i].varValue for i in range(num_vertices))
    print(int(clique_size))

if __name__ == "__main__":
    num_vertices, num_edges = map(int, input().split())
    graph_dict = dict()

    for i in range(num_vertices):
        graph_dict[i] = []

    for i in range(num_edges):
        c1, c2 = input().strip().split()
        c1, c2 = int(c1), int(c2)

        graph_dict[c1].append(c2)

        graph_dict[c2].append(c1)

    max_clique_size(graph_dict, num_vertices)

    


# in
# 3 3
# 0 1
# 0 2
# 1 2

# out
# 3


#in
# 6 3
# 0 3
# 1 4
# 2 4

# out
# 2


