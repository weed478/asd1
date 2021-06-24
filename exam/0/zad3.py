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
from zad3testy import runtests


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

    # jump_edges[u][v] = waga *najlepszego* skoku 2 krawędziami z u do v
    jump_edges = [[inf] * n for _ in range(n)]

    # bierzemy 2 wierzchołki i jeden pośredni do skoku
    for u in range(n):
        for v in range(n):
            for w in range(n):
                if u == v or u == w or v == w:
                    continue

                # if można skoczyć
                if G[u][w] != 0 and G[w][v] != 0:
                    # szukamy najlepszego pośredniego wierzchołka więc min
                    jump_edges[u][v] = min(jump_edges[u][v],
                                           max(G[u][w], G[w][v]))

    # bellman-ford
    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                # relaksacja dla ścieżki kończącej się skokiem
                # jump edges ma domyślnie inf więc nie trzeba sprawdzać czy istnieje skok
                d[v].jump = min(d[v].jump,
                                d[u].normal + jump_edges[u][v])

                # relaksacja dla ścieżki kończącej się normalnym ruchem
                if G[u][v] != 0:
                    d[v].normal = min(d[v].normal,
                                      d[u].min() + G[u][v])  # d[u].min() to albo skok albo normalny

    return d[target].min()


if __name__ == "__main__":
    G1 = [[0, 1, 0, 0, 0],
          [1, 0, 1, 0, 0],
          [0, 1, 0, 7, 0],
          [0, 0, 7, 0, 8],
          [0, 0, 0, 8, 0]]

    G2 = [[0, 1, 3, 0],
          [1, 0, 1, 2],
          [3, 1, 0, 4],
          [0, 2, 4, 0]]

    print(jumper(G2, 0, 3))

    runtests(jumper)
