from math import inf
from queue import PriorityQueue


def dijkstra(G, s):
    n = len(G)

    parent = [None] * n
    visited = [False] * n
    d = [inf] * n
    d[s] = 0
    Q = PriorityQueue()

    for u in range(n):
        Q.put((0 if u == s else inf, u))

    while not Q.empty():
        _, u = Q.get()
        if visited[u]:
            continue
        visited[u] = True

        for (v, w_uv) in G[u]:
            if d[u] + w_uv < d[v]:
                d[v] = d[u] + w_uv
                parent[v] = u
                Q.put((d[v], v))

    return d, parent


if __name__ == "__main__":
    G = [[(1, 1)],
         [(0, 1), (3, 1), (5, 1)],
         [(3, 1)],
         [(1, 1), (2, 1), (4, 1), (5, 1)],
         [(3, 1), (5, 1), (6, 1)],
         [(1, 1), (3, 1), (4, 1), (6, 1), (7, 1)],
         [(5, 1), (4, 1), (7, 1), (8, 1)],
         [(5, 1), (6, 1), (8, 1)],
         [(6, 1), (7, 1)]]

    d, p = dijkstra(G, 1)
    print(d, p)

    G = [[(1, 1)],
         [(0, 1), (3, 0), (5, 1)],
         [(3, 1)],
         [(1, 0), (2, 1), (4, 0), (5, 1)],
         [(3, 0), (5, 0), (6, 1)],
         [(1, 1), (3, 1), (4, 0), (6, 0), (7, 1)],
         [(5, 0), (4, 1), (7, 1), (8, 0)],
         [(5, 1), (6, 1), (8, 0)],
         [(6, 0), (7, 0)]]

    d, p = dijkstra(G, 1)
    print(d, p)
