from unionfind import Node, find, union


def weight(e):
    return e[2]


def kruskal(G):
    n = len(G)
    G.sort(key=weight)

    vert = [None] + [Node(i) for i in range(n)]

    S = []

    for e in G:
        if find(vert[e[0]]) != find(vert[e[1]]):
            union(vert[e[0]], vert[e[1]])
            S.append((e[0], e[1]))

    return S


# edge list
G = [(1, 2, 3),
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

print(kruskal(G))
