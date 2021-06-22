from math import inf
from unionfind import Node, find, union
from heap import Heap
from index_array import IndexArray
from graph_conv import edges_to_adj


def weight(e):
    return e[2]


def kruskal(G, n):
    G.sort(key=weight)
    vert = [Node(i) for i in range(n)]
    S = []

    for e in G:
        if find(vert[e[0]]) != find(vert[e[1]]):
            union(vert[e[0]], vert[e[1]])
            S.append((e[0], e[1]))

    return S


def prim(adj, r):
    n = len(adj)

    d = [inf] * n
    parent = [None] * n
    in_queue = [True] * n

    heap = IndexArray(n)
    Q = Heap(heap, lambda u, v: d[u] < d[v])

    d[r] = 0
    Q.build()

    while len(Q) > 0:
        u = Q.extract_top()
        in_queue[u] = False
        for (v, w_uv) in adj[u]:
            if in_queue[v] and w_uv < d[v]:
                d[v] = w_uv
                Q.increase_key(heap.index_of(v), v)
                parent[v] = u

    return parent


if __name__ == "__main__":
    # edge list
    G = [(0, 1, 1),
         (1, 2, 3),
         (1, 4, 7),
         (3, 4, 12),
         (2, 3, 7),
         (2, 6, 1),
         (3, 6, 8),
         (3, 5, 2),
         (4, 5, 4),
         (5, 7, 10),
         (5, 8, 6),
         (7, 8, 5)]

    print(kruskal(G, 9))
    print(prim(edges_to_adj(G), 1))
