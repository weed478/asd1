from math import inf


def jump_cost(a, b):
    for d in str(a):
        if d in str(b):
            return abs(a - b)
    return inf


def min_jump_cost(T):
    n = len(T)

    s = min(range(n), key=T.__getitem__)
    t = max(range(n), key=T.__getitem__)

    # dijkstra

    visited = [False] * n
    d = [inf] * n
    d[s] = 0

    for _ in range(n):
        u = min(range(n), key=lambda u: inf if visited[u] else d[u])
        visited[u] = True

        for v in range(n):
            cost = jump_cost(T[u], T[v])
            d[v] = min(d[v], d[u] + cost)

    return d[t]


if __name__ == "__main__":
    print(min_jump_cost([123, 890, 688, 587, 257, 246]))  # 767
    print(min_jump_cost([587, 990, 257, 246, 668, 132]))  # inf
