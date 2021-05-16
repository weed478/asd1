def find_mosty(adj):
    n = len(adj)

    parents = [None] * n
    visited_time = [None] * n
    low = [None] * n
    t = 0

    def dfs(v, p):
        parents[v] = p
        nonlocal t
        visited_time[v] = t
        low[v] = t
        t += 1
        for u in adj[v]:
            if u == p:
                continue

            if visited_time[u] is None:
                low[v] = min(low[v], dfs(u, v))
            else:
                low[v] = min(low[v], visited_time[u])

        return low[v]

    for v in range(n):
        if visited_time[v] is None:
            dfs(v, v)

    bridges = []

    for v in range(n):
        if visited_time[v] == low[v] and v != parents[v]:
            bridges.append((v, parents[v]))

    return bridges


G = [[7],  # 0
     [2, 3],  # 1
     [1, 4],  # 2
     [1, 4],  # 3
     [2, 3, 7],  # 4
     [7, 6],  # 5
     [7, 5],  # 6
     [4, 0, 5, 6]]  # 7

print(find_mosty(G))
