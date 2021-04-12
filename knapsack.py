def get_solution(F, W, P, i, w):
    if i == 0:
        return [0] if W[0] <= w else []

    if W[i] <= w and F[i][w] == F[i - 1][w - W[i]] + P[i]:
        return get_solution(F, W, P, i - 1, w - W[i]) + [i]
    else:
        return get_solution(F, W, P, i - 1, w)


def knapsack(W, P, max_w):
    if max_w == 0:
        return []

    n = len(W)

    F = [[0] * (max_w + 1) for _ in range(n)]

    for w in range(W[0], max_w + 1):
        F[0][w] = P[0]

    for i in range(1, n):
        for w in range(1, max_w + 1):
            F[i][w] = max(F[i - 1][w], F[i - 1][w - W[i]] + P[i] if w >= W[i] else 0)

    print(get_solution(F, W, P, n - 1, max_w))


knapsack([4, 5, 12, 9, 1, 13], [10, 8, 4, 5, 3, 7], 19)
