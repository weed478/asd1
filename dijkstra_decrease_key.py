from math import inf
from heap import Heap
from index_array import IndexArray


def dijkstra(adj, s):
    n = len(adj)

    d = [inf] * n
    parent = [None] * n

    heap = IndexArray(n)
    Q = Heap(heap, lambda u, v: d[u] < d[v])

    d[s] = 0
    Q.build()

    while len(Q) > 0:
        u = Q.extract_top()
        for (v, w) in adj[u]:
            # relax
            if d[u] + w < d[v]:
                d[v] = d[u] + w
                Q.increase_key(heap.index_of(v), v)
                parent[v] = u

    return d


if __name__ == "__main__":
    G = [[(1, 1), (2, 5)],
         [(0, 1), (2, 2), (3, 8), (4, 7)],
         [(0, 5), (1, 2), (3, 3)],
         [(2, 3), (1, 8), (4, 1)],
         [(1, 7), (3, 1)]]

    d = dijkstra(G, 0)
    assert d == [0, 1, 3, 6, 7]
    print(d)
