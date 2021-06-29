"""
Jakub Karbowski

1. Liczymy odległości każdy do każdego
2. Tworzymy sieć przepływową do policzenia skojarzeń
3. Tak

Złożoność zasadniczo ograniczana Edmondsem-Karpem do O(VE^2).
Nie będzie szybciej nić O(V^3) przez budowanie sieci przepływowej.
Zamienienie floyda-warshalla na dijkstrę dla każdego wierzchołka i tak robi O(V^3).

Pamięciowo alokujemy V^2.
"""

from zad3testy import runtests
from zad3EK import edmonds_karp
from math import inf


def floyd_warshall(M):
    n = len(M)
    dist = [[inf for _ in range(n)] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if M[u][v] == 0:
                dist[u][v] = inf
            else:
                dist[u][v] = M[u][v]
        dist[u][u] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def BlueAndGreen(T, K, D):
    n = len(T)

    # O(V^3)
    d = floyd_warshall(T)

    nf = n + 2
    Gf = [[0 for _ in range(nf)] for _ in range(nf)]
    supersource = nf - 1
    supersink = nf - 2

    # O(V^2)
    for u in range(n):
        if K[u] != 'G':
            continue
        # for every green 'u'

        Gf[supersource][u] = 1

        # O(V)
        for v in range(n):
            if K[v] != 'B' or d[u][v] < D:
                continue
            # for every blue 'v' farther than D from u

            Gf[u][v] = 1
            Gf[v][supersink] = 1

    # O(VE^2)
    flow = edmonds_karp(Gf, supersource, supersink)

    return flow


runtests(BlueAndGreen)
