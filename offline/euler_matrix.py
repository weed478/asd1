"""
O(V^2)
"""


def has_euler(G):
    n = len(G)

    visited = [False] * n
    even_rule_broken = False

    def dfs(u):
        visited[u] = True
        even = True
        for v in range(n):
            if G[u][v] != 0:
                even = not even
                if not visited[v]:
                    dfs(v)

        if not even:
            nonlocal even_rule_broken
            even_rule_broken = True

    dfs(0)

    return not even_rule_broken and False not in visited


def euler(G):
    # O(V^2)
    if not has_euler(G):
        return None

    n = len(G)

    visited_edges = [[False] * n for _ in range(n)]
    checked = [0] * n
    cycle = []

    def dfs(u):
        for v in range(checked[u], n):
            checked[u] = v + 1

            if G[u][v] == 0 or visited_edges[u][v]:
                continue

            visited_edges[u][v] = True
            visited_edges[v][u] = True

            dfs(v)

        cycle.append(u)

    dfs(0)

    return cycle


def check_euler(cycle, G):
    n = len(G)
    visited_edges = [[False] * n for _ in range(n)]
    u = cycle[0]
    for v in cycle[1:]:
        if visited_edges[u][v] or G[u][v] == 0:
            return False
        visited_edges[u][v] = True
        visited_edges[v][u] = True
        u = v
    return True


if __name__ == "__main__":
    G1 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 1, 1, 0, 1],
          [1, 1, 0, 0, 1, 1],
          [0, 1, 0, 0, 0, 1],
          [0, 0, 1, 0, 0, 1],
          [0, 1, 1, 1, 1, 0]]

    cycle = euler(G1)
    print(cycle)
    print(check_euler(cycle, G1))
