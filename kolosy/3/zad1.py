"""
Jakub Karbowski

Algorytm:
1. Liczymy odległości każdy do każdego wierzchołka
2. Budujemy graf G reprezentowany listą sąsiedztwa gdzie:
   - wierzchołek to para liczb reprezentująca ustawienie Carol i Max
   - każda krawędź to krotka (nowe_ustawienie, koszt przejścia do nowego ustawienia)

3. Algorytmem dijkstry szukamy najkrótszej ścieżki w nowym grafie (zwykły DFS ponieważ nie trzeba jednak szukać najlepszej)

Złożoność:
Ograniczeniem jest algorytm dijsktry O(ElogV) (graf G jako lista sąsiedztwa)

W grafie G liczba wierzchołków to n*n
gdzie n to liczba wierzchołków w grafie wejściowym

W najgorszym przypadku (E = V^2)
złożoność to O(n^4 * log(n^2))

W przypadku ogólnym E jest zdecydowanie mniejsze.
Można ulepszyć złożoność Dijkstry do O(V^2) dla macierzy sąsiedztwa
budując tym sposobem graf G, ale używając więcej pamięci.

Pamięciowo zajmujemy n^2

----- Errata
A czyli jednak nie trzeba najkrótszej ścieżki.
Zamiast Dijkstry zwykły DFS.

Złożoność O(V+E) czyli O(n^2 + E) gdzie E tak jak powyżej.
"""


from zad1testy import runtests
from math import inf
from queue import PriorityQueue


# zwykły dijkstra ale wierzchołek to para liczb
def dijkstra(adj, s):
    n = len(adj)

    d = [[inf for u in range(n)] for v in range(n)]
    parent = [[None for u in range(n)] for v in range(n)]
    visited = [[False for u in range(n)] for v in range(n)]

    Q = PriorityQueue()

    for u in range(n):
        for v in range(n):
            if (u, v) == s:
                Q.put((0, (u, v)))
                d[u][v] = 0
            else:
                Q.put((inf, (u, v)))

    while not Q.empty():
        _, (u, v) = Q.get()
        if visited[u][v]:
            continue

        visited[u][v] = True

        # relaksacja dla pary liczb gdzie waga to suma wag przejścia miedzy stanami Carol i Max
        for ((u_prim, v_prim), uv_prim_w) in adj[u][v]:
            if d[u][v] + uv_prim_w < d[u_prim][v_prim]:
                d[u_prim][v_prim] = d[u][v] + uv_prim_w
                Q.put((d[u_prim][v_prim], (u_prim, v_prim)))
                parent[u_prim][v_prim] = (u, v)

    return d, parent


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


def rebuild_path(u, v, parent):
    if parent[u][v] is None:
        return [(u, v)]

    return rebuild_path(parent[u][v][0], parent[u][v][1], parent) + [(u, v)]


def dfs(G, u0, v0):
    n = len(G)

    parent = [[None for u in range(n)] for v in range(n)]
    visited = [[False for u in range(n)] for v in range(n)]

    def _dfs(u, v):
        for ((up, vp), _) in G[u][v]:
            if not visited[up][vp]:
                visited[up][vp] = True
                parent[up][vp] = (u, v)
                _dfs(up, vp)

    visited[u0][v0] = True
    _dfs(u0, v0)

    return None, parent


def keep_distance(M, x, y, d):
    n = len(M)

    G = [[[] for u in range(n)] for v in range(n)]

    dist = floyd_warshall(M)

    def build_G(u, v):
        for u_prim in range(n):
            for v_prim in range(n):
                if (M[u][u_prim] != 0 or u == u_prim) and \
                   (M[v][v_prim] != 0 or v == v_prim) and \
                   dist[u_prim][v_prim] >= d and \
                   (not (u_prim == v and v_prim == u)):

                    # dodajemy krawędź między ustawieniami uv i uv_prim jeśli:
                    # - jest krawędz z u do u_prim i v do v_prim (lub stoimy w miejscu)
                    # - odległość (separacja) w nowym ustawieniu >= d
                    # - nie idziemy tą samą krawędzią w przeciwnych kierunkach

                    G[u][v].append(((u_prim, v_prim), M[u][u_prim] + M[v][v_prim]))

    for u in range(n):
        for v in range(n):
            build_G(u, v)

    d, parent = dijkstra(G, (x, y))

    # zamiast dijkstry DFS ale zostawiłem dijkstrę bo ładnie działa (DFS oczywiście też)
    # d, parent = dfs(G, x, y)

    return rebuild_path(y, x, parent)


runtests(keep_distance)
