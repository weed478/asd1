from math import inf
from graph_conv import max_vertex


def bellman_ford(E, n, s):
    d = [inf] * n
    d[s] = 0

    def relax(u, v, w):
        if d[u] + w < d[v]:
            d[v] = d[u] + w

    for i in range(n - 1):
        for (u, v, w) in E:
            relax(u, v, w)

    for (u, v, w) in E:
        if d[v] > d[u] + w:
            return "Negative cycle"

    return d


E = [(0, 1, 1),
     (1, 2, -3),
     (1, 4, 7),
     (3, 4, -12),
     (2, 3, 7),
     (2, 6, 1),
     (3, 6, -8),
     (3, 5, 2),
     (4, 5, 4),
     (5, 7, 10),
     (5, 8, -6),
     (7, 8, 5)]

print(bellman_ford(E, max_vertex(E) + 1, 0))
