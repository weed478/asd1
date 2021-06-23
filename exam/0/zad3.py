from math import inf


class Dist:
    def __init__(self):
        self.normal = inf
        self.jump = inf

    def min(self):
        return min(self.normal, self.jump)


def jumper(G, source, target):
    n = len(G)

    d = [Dist() for _ in range(n)]
    d[source].normal = 0
    d[source].jump = 0

    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if G[u][v] == 0:
                    continue

                for w in range(n):
                    if G[w][u] == 0:
                        continue

                    d[v].jump = min(d[v].jump,
                                    d[w].normal + max(G[w][u], G[u][v]))

                d[v].normal = min(d[v].normal,
                                  d[u].min() + G[u][v])

    return d[target].min()


if __name__ == "__main__":
    G1 = [[0, 1, 0, 0, 0],
          [1, 0, 1, 0, 0],
          [0, 1, 0, 7, 0],
          [0, 0, 7, 0, 8],
          [0, 0, 0, 8, 0]]

    print(jumper(G1, 0, 4))
