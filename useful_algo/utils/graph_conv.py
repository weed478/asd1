def max_vertex(E):
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    return n


def edges_to_adj(E, undirected=True):
    n = max_vertex(E) + 1
    adj = [[] for _ in range(n)]

    for e in E:
        if len(e) == 2:
            adj[e[0]].append(e[1])
            if undirected:
                adj[e[1]].append(e[0])
        elif len(e) == 3:
            adj[e[0]].append((e[1], e[2]))
            if undirected:
                adj[e[1]].append((e[0], e[2]))

    return adj
