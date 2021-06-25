from math import inf


def floyd_warshall(G):
    n = len(G)
    dist = [[inf for _ in range(n)] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if G[u][v] == 0:
                dist[u][v] = inf
            else:
                dist[u][v] = G[u][v]
        dist[u][u] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j])

    return dist


if __name__ == "__main__":
    G1 = [[0, 1, 1, 8],
          [0, 0, 1, 0],
          [1, 0, 0, 1],
          [0, 0, 0, 0]]

    for row in floyd_warshall(G1):
        print(row)
