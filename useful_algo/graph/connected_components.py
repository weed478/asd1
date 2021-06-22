def find_scc(adj):
    n = len(adj)

    visited = [False] * n
    processed_order = []

    def dfs(v):
        visited[v] = True
        for u in adj[v]:
            if not visited[u]:
                dfs(u)
        processed_order.append(v)

    for v in range(n):
        if not visited[v]:
            dfs(v)

    rev_adj = [[] for _ in range(n)]
    for v in range(n):
        for u in adj[v]:
            rev_adj[u].append(v)

    visited = [False] * n
    scc = []

    def dfs(v):
        visited[v] = True
        scc[-1].append(v)
        for u in rev_adj[v]:
            if not visited[u]:
                dfs(u)

    for v in reversed(processed_order):
        if not visited[v]:
            scc.append([])
            dfs(v)

    return scc


if __name__ == "__main__":
    G = [[],  # 0
         [3],  # 1
         [1],  # 2
         [2, 0, 4, 9],  # 3
         [6],  # 4
         [4],  # 5
         [5, 7],  # 6
         [4],  # 7
         [9],  # 8
         [4, 10],  # 9
         [11],  # 10
         [8, 7]]  # 11

    print(find_scc(G))
