from queue import PriorityQueue
from math import inf


def dijkstra(G, A, B):
    n = len(G)

    d = [inf] * n
    d[A] = 0

    visited = [False] * n

    Q = PriorityQueue()
    for u in range(n):
        Q.put((0 if u == A else inf, u))

    while not Q.empty():
        _, u = Q.get()
        if visited[u]:
            continue

        visited[u] = True
        for v in range(n):
            if G[u][v] > 0:
                if d[u] + G[u][v] < d[v]:
                    d[v] = d[u] + G[u][v]
                    Q.put((d[v], v))

    return d


if __name__ == "__main__":
    G1 = [[0, 5, 1, 8, 0, 0, 0],
          [5, 0, 0, 1, 0, 8, 0],
          [1, 0, 0, 8, 0, 0, 8],
          [8, 1, 8, 0, 5, 0, 1],
          [0, 0, 0, 5, 0, 1, 0],
          [0, 8, 0, 0, 1, 0, 5],
          [0, 0, 8, 1, 0, 5, 0]]

    print(dijkstra(G1, 5, 2))
