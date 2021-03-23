from random import choices


def partition(A, p, r):
    i = p
    j = p
    k = r

    while j < k:
        if A[j] < A[p]:
            A[p], A[j] = A[j], A[p]
            i = p + 1
            j += 1

        elif A[j] > A[r - 1]:
            A[r - 1], A[j] = A[j], A[r - 1]
            k = r - 1

        elif A[j] == A[p]:
            A[i], A[j] = A[j], A[i]
            i += 1
            j += 1

        elif A[j] == A[r - 1]:
            k -= 1
            A[k], A[j] = A[j], A[k]

        else:
            j += 1

    return i, k


def sort(A, p, r):
    while r - p > 1:
        p, r = partition(A, p, r)


if __name__ == "__main__":
    t = choices(range(4), k=30)
    print(t)
    sort(t, 0, len(t))
    print(t)
    assert sorted(t) == t
