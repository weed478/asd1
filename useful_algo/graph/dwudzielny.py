def dwudzielny(G):
    n = len(G)
    visited = [None] * n

    def dfs(i, color):
        for v in G[i]:
            if visited[v] is None:
                visited[v] = color
                if not dfs(v, not color):
                    return False
            elif visited[v] != color:
                return False

        return True

    return dfs(0, False)


k33 = [
    [3, 4, 5],
    [3, 4, 5],
    [3, 4, 5],

    [0, 1, 2],
    [0, 1, 2],
    [0, 1, 2]
]

print(dwudzielny(k33))
