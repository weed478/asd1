def get_solution(F, W, P, i, w):
    if i == 0:
        return [0] if W[0] <= w else []

    if W[i] <= w and F[i][w] == F[i - 1][w - W[i]] + P[i]:
        return get_solution(F, W, P, i - 1, w - W[i]) + [i]
    else:
        return get_solution(F, W, P, i - 1, w)


def knapsack1(W, P, max_w):
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


def get_solution2(F, W, P, i, w, p):
    if i == 0:
        return [0] if W[0] <= w else []

    if W[i] <= w and F[i - 1][p - P[i]] == F[i][p] - W[i]:
        return get_solution2(F, W, P, i - 1, w - W[i], p - P[i]) + [i]
    else:
        return get_solution2(F, W, P, i - 1, w, p)


def knapsack2(W, P, max_w):
    if max_w == 0:
        return []

    n = len(W)
    max_p = sum(P)

    """
    F[i][p] = ile najmniej waży zestaw mający profit p używający elementów 0-i mieszcząc się w max_w (-1 jak się nie da)
    F[0][p] = W[0] if W[0] <= max_w and P[0] >= p else -1
    F[i][0] = 0
    F[i][p] = min{
        if F[i - 1][p] > -1
            F[i - 1][p]
        ,    
        if F[i - 1][p - P[i]] > -1
            F[i - 1][p - P[i]] + W[i]
        }
        or -1
    """

    F = [[-1] * (max_p + 1) for _ in range(n)]

    for p in range(max_p + 1):
        F[0][p] = W[0] if W[0] <= max_w and P[0] >= p else -1

    for i in range(n):
        F[i][0] = 0

    for i in range(1, n):
        for p in range(1, max_p + 1):
            F[i][p] = max_w + 1
            if F[i - 1][p] > -1:
                F[i][p] = min(F[i][p], F[i - 1][p])

            if F[i - 1][p - P[i]] > -1:
                F[i][p] = min(F[i][p], F[i - 1][p - P[i]] + W[i])

            if F[i][p] == max_w + 1:
                F[i][p] = -1

    best_p = 0
    for p in range(0, max_p + 1):
        if -1 < F[n - 1][p] <= max_w and p > best_p:
            best_p = p

    print(best_p)
    print(get_solution2(F, W, P, n - 1, max_w, best_p))


knapsack1([4, 5, 12, 9, 1, 13], [10, 8, 4, 5, 3, 7], 19)
knapsack2([4, 5, 12, 9, 1, 13], [10, 8, 4, 5, 3, 7], 19)
