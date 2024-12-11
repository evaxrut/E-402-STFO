# m4p2
# Write code that given a graph G uses integer linear programming to find the size of the largest independent set. The graph is given as a dictionary of adjacency sets. An independent set is a subset of vertices where no vertex is connected to any other vertex. G has at most 25 vertices. G is given in the same way as in m4p1.

import pulp

def max_independent_set(graph_dict, num_verticies):
    # all_vertices = set(graph_dict)
    p = pulp.LpProblem("Example", pulp.LpMaximize)

    v = pulp.LpVariable.dict("x", range(num_verticies), cat="Binary")

    # objective
    p += pulp.lpSum(v[i] for i in range(num_verticies))

    # subject to
    for i in range(num_verticies):
        connected_to = set(graph_dict.get(i, []))
        # not_connected = all_vertices.difference(connected_to) - {i}
        for j in connected_to:
            p += v[i] + v[j] <= 1

    p.solve(pulp.PULP_CBC_CMD(msg=False))

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

    max_independent_set(graph_dict, num_vertices)