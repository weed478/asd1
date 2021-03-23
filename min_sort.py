def min_partition(A, p, r):
    i = p + 1
    j = p + 1

    while j < r:
        if A[j] < A[p]:
            A[p], A[j] = A[j], A[p]
            i = p + 1

        elif A[j] == A[p]:
            A[i], A[j] = A[j], A[i]
            i += 1

        j += 1

    return i


def sort(A, p, r):
    while r - p > 1:
        p = min_partition(A, p, r)
