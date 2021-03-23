from math import log, ceil
from random import choices


def partition(A, p, r, x):
    i = p
    j = p

    for k in range(p, r):
        if x < A[k]:
            continue
        elif A[k] < x:
            A[j], A[k] = A[k], A[j]
            A[i], A[j] = A[j], A[i]
            i += 1
            j += 1
        else:
            A[j], A[k] = A[k], A[j]
            j += 1

    return i, j


def qsort(A, p, r):
    while r - p > 1:
        i, j = partition(A, p, r, A[p])

        if i - p > r - j:
            r = i
            qsort(A, j, r)
        else:
            qsort(A, p, i)
            p = j


def gen_data(n):
    return choices(range(ceil(log(n, 2))), k=n)


if __name__ == "__main__":
    t = gen_data(30)
    print(t)
    qsort(t, 0, len(t))
    print(t)
