from math import inf


def opt_sum(t):
    """
    f(i, j) = najlepsza pośrednia wartość bezwzględna dodająca elementy i do j
    f(i, j) = min{k}( max( |g(i, k) + g(k + 1, j)|, f(i, k), f(k + 1, j) ) )
    f(i, i) = 0

    g(i, j) = suma elementów od i do j
    """

    n = len(t)

    F = [[None for _ in range(n)] for _ in range(n)]
    G = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        F[i][i] = 0

    def g(i, j):
        if G[i][j] is None:
            G[i][j] = sum(t[i:j + 1])
        return G[i][j]

    def f(i, j):
        if F[i][j] is None:
            best = inf
            for k in range(i, j):
                best = min(best, max(
                    abs(g(i, k) + g(k + 1, j)),
                    f(i, k),
                    f(k + 1, j)))
            F[i][j] = best

        return F[i][j]

    return f(0, n - 1)


if __name__ == "__main__":
    print(opt_sum([1, -5, 2]))  # 3
