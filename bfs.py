from collections import deque
from math import inf


# can get stuck with w=0
def recreate_shortest_binary_path(v0, v1, d, adj):
    path = [v1]
    while v0 != v1:
        for (v, w) in adj[v1]:
            if d[v] == d[v1] - w:
                v1 = v
                path.append(v)
                break
        else:
            return None
    path.reverse()
    return path


def backtrack_shortest_path(vk, p):
    path = [vk]
    while p[vk] is not None:
        vk = p[vk]
        path.append(vk)
    path.reverse()
    return path


def shortest_binary_path(v0, adj):
    n = len(adj)

    q = deque()
    d = [inf] * n

    q.append(v0)
    d[v0] = 0

    parents = [None] * n

    while len(q) > 0:
        v = q.popleft()
        for (u, w) in adj[v]:
            if d[v] + w < d[u]:
                d[u] = d[v] + w
                parents[u] = v
                if w == 0:
                    q.appendleft(u)
                else:
                    q.append(u)

    return d, parents


G = [[(1, 1)],
     [(0, 1), (3, 1), (5, 1)],
     [(3, 1)],
     [(1, 1), (2, 1), (4, 1), (5, 1)],
     [(3, 1), (5, 1), (6, 1)],
     [(1, 1), (3, 1), (4, 1), (6, 1), (7, 1)],
     [(5, 1), (4, 1), (7, 1), (8, 1)],
     [(5, 1), (6, 1), (8, 1)],
     [(6, 1), (7, 1)]]

d, p = shortest_binary_path(1, G)
print(d, p)
print(backtrack_shortest_path(7, p))

G = [[(1, 1)],
     [(0, 1), (3, 0), (5, 1)],
     [(3, 1)],
     [(1, 0), (2, 1), (4, 0), (5, 1)],
     [(3, 0), (5, 0), (6, 1)],
     [(1, 1), (3, 1), (4, 0), (6, 0), (7, 1)],
     [(5, 0), (4, 1), (7, 1), (8, 0)],
     [(5, 1), (6, 1), (8, 0)],
     [(6, 0), (7, 0)]]

d, p = shortest_binary_path(1, G)
print(d, p)
print(backtrack_shortest_path(7, p))
