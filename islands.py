from math import inf


def islands(G, A, B):
    n = len(G)

    d = [[inf, inf, inf] for _ in range(n)]
    d[A] = [0, 0, 0]

    def relax(u, v, f, t, w):
        if d[u][f] + w < d[v][t]:
            d[v][t] = d[u][f] + w

    for i in range(n - 1):
        for u in range(n):
            for v in range(n):
                w = G[u][v]
                if w == 0:
                    continue

                if w == 1:
                    relax(u, v, 1, 0, w)
                    relax(u, v, 2, 0, w)

                elif w == 5:
                    relax(u, v, 0, 1, w)
                    relax(u, v, 2, 1, w)

                elif w == 8:
                    relax(u, v, 0, 2, w)
                    relax(u, v, 1, 2, w)

    return min(d[B])


if __name__ == "__main__":
    G1 = [[0, 5, 1, 8, 0, 0, 0],
          [5, 0, 0, 1, 0, 8, 0],
          [1, 0, 0, 8, 0, 0, 8],
          [8, 1, 8, 0, 5, 0, 1],
          [0, 0, 0, 5, 0, 1, 0],
          [0, 8, 0, 0, 1, 0, 5],
          [0, 0, 8, 1, 0, 5, 0]]

    G2 = [[0, 5, 8, 0, 0, 0, 0],
          [5, 0, 0, 8, 0, 0, 0],
          [8, 0, 0, 1, 0, 0, 0],
          [0, 8, 1, 0, 1, 5, 0],
          [0, 0, 0, 1, 0, 0, 5],
          [0, 0, 0, 5, 0, 0, 8],
          [0, 0, 0, 0, 5, 8, 0]]

    print(islands(G2, 0, 6))
