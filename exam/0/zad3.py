"""
Bellman-Ford gdzie liczymy najlepszą drogę
kończąc skokiem i normalnym ruchem.
Na początku obliczamy jump_edges żeby potem było szybciej.

O(V^3) time
O(V^2) memory

Albo (bez liczenia jump_edges)
O(V^4) time
O(V) memory
"""

from math import inf


class Dist:
    def __init__(self):
        # najlepsza droga kończąc normalnym ruchem i skokiem
        self.normal = inf
        self.jump = inf

    def min(self):
        return min(self.normal, self.jump)


def jumper(G, source, target):
    n = len(G)

    d = [Dist() for _ in range(n)]
    d[source].normal = 0
    d[source].jump = 0

    # jump_edges[u][v] = waga skoku 2 krawędziami z u do v
    jump_edges = [[0] * n for _ in range(n)]

    # bierzemy 2 wierzchołki i jeden pośredni do skoku
    for u in range(n):
        for v in range(n):
            for w in range(n):
                # if można skoczyć
                if G[u][w] > 0 and G[w][v] > 0:
                    jump_edges[u][v] = max(G[u][w], G[w][v])

    # bellman-ford
    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                # relaksacja dla ścieżki kończącej się skokiem
                if jump_edges[u][v]:
                    d[v].jump = min(d[v].jump,
                                    d[u].normal + jump_edges[u][v])

                # relaksacja dla ścieżki kończącej się normalnym ruchem
                if G[u][v] > 0:
                    d[v].normal = min(d[v].normal,
                                      d[u].min() + G[u][v])  # d[u].min() to albo skok albo normalny

    return d[target].min()


if __name__ == "__main__":
    G1 = [[0, 1, 0, 0, 0],
          [1, 0, 1, 0, 0],
          [0, 1, 0, 7, 0],
          [0, 0, 7, 0, 8],
          [0, 0, 0, 8, 0]]

    print(jumper(G1, 0, 4))
