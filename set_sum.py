def get_solution(A, F, i, s):
    if i == 0:
        return [0] if A[0] == s else []

    if F[i][s] and not F[i - 1][s]:
        return get_solution(A, F, i - 1, s - A[i]) + [i]
    else:
        return get_solution(A, F, i - 1, s)


def set_sum(A, T):
    n = len(A)
    F = [[None] * (T + 1) for _ in range(n)]
    """
    F[i][s] = czy można uzyskać sumę s używając elementów 0-i
    F[0][s] = A[0] == s
    F[i][0] = True
    
    F[i][s] = F[i - 1][s - A[i]] or F[i - 1][s]
    """

    for s in range(0, T + 1):
        F[0][s] = A[0] == s

    for i in range(n):
        F[i][0] = True

    for i in range(1, n):
        for s in range(1, T + 1):
            F[i][s] = F[i][s] or F[i - 1][s] or (s - A[i] >= 0 and F[i - 1][s - A[i]])

    return get_solution(A, F, n - 1, T)


t = [10, 8, 4, 5, 3, 7]
s = 24
set = set_sum(t, s)
print(set)
assert sum(map(lambda i: t[i], set)) == s
