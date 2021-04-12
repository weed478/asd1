def print_lis(A, F, P, n, m, current):
    if m == 0:
        print(list(reversed(current)))
        return 1
    else:
        count = 0
        for i in range(n):
            if F[i] == m:
                count += print_lis(A, F, P, i, m - 1, current + [A[i]])
        return count


def lis(A):
    n = len(A)
    F = [1] * n
    P = [[] for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i]:
                F[i] = max(F[j] + 1, F[i])
                P[i].append(j)

    m = max(F)
    return print_lis(A, F, P, n, m, [])


# t = [3, 1, 5, 7, 2, 4, 9, 3, 17, 3]
t = [2, 1, 4, 3]
print(lis(t))

