def euler(adj):
    n = len(adj)

    visited_edges = [[False] * n for _ in range(n)]
    cycle = []

    def dfs(v):
        for u in adj[v]:
            if visited_edges[v][u]:
                continue

            visited_edges[v][u] = True
            visited_edges[u][v] = True

            dfs(u)

        cycle.append(v)

    dfs(0)

    return cycle


G = [[1, 2],
     [0, 2, 3, 4],
     [0, 1, 3, 5],
     [1, 4, 5, 2],
     [1, 3, 5, 6],
     [2, 3, 4, 6],
     [5, 4]]

print(euler(G))
