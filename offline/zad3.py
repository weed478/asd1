from random import randint, shuffle, seed


def partition(A, p, r):
    i = p - 1

    for j in range(p, r):
        if A[j] <= A[r - 1]:
            i += 1
            A[i], A[j] = A[j], A[i]

    return i


def insertion_sort(A, p, r):
    for i in range(p + 1, r):
        for j in range(i, p, -1):
            if A[j - 1] > A[j]:
                A[j - 1], A[j] = A[j], A[j - 1]
            else:
                break


def pivot5(A, p, r):
    insertion_sort(A, p, r)
    return (p + r) // 2


def median_of_medians(A, p, r):
    n = r - p
    bins = (n + 4) // 5
    for i in range(bins):
        left = p + i * 5
        right = min(left + 5, r)
        median = pivot5(A, left, right)
        A[p + i], A[median] = A[median], A[p + i]

    return linear_select(A, p, p + bins, p + bins // 2)


def pivot(A, p, r):
    if r - p <= 5:
        return pivot5(A, p, r)
    else:
        return median_of_medians(A, p, r)


def linear_select(A, p, r, k):
    while r - p > 1:
        x = pivot(A, p, r)
        A[x], A[r - 1] = A[r - 1], A[x]
        q = partition(A, p, r)

        if k < q:
            r = q
        elif q < k:
            p = q + 1
        else:
            return q

    return p


def linearselect(A, k):
    return linear_select(A, 0, len(A), k)


seed(42)

n = 11
for i in range(n):
    A = list(range(n))
    shuffle(A)
    print(A)
    x = linearselect(A, i)
    if x != i:
        print("Blad podczas wyszukiwania liczby", i)
        exit(0)

print("OK")
