from random import randint, seed


def partition(t, p, r):
    x = t[r - 1]
    i = p - 1
    for j in range(p, r):
        if t[j] <= x:
            i += 1
            t[i], t[j] = t[j], t[i]
    return i


def quicksort(t, p, r):
    while r - p > 1:
        q = partition(t, p, r)
        if q - p < r - q - 1:
            quicksort(t, p, q)
            p = q + 1
        else:
            quicksort(t, q + 1, r)
            r = q


def qsort(t):
    t = t.copy()
    quicksort(t, 0, len(t))
    return t


def test_sort():
    assert qsort([1]) == [1]
    assert qsort([1, 2]) == [1, 2]
    assert qsort([2, 1]) == [1, 2]
    assert qsort([2, 1, 3]) == [1, 2, 3]
    for n in range(100):
        t = [randint(-10, 10) for _ in range(n)]
        assert qsort(t) == sorted(t)
    print("Pass")


def speed(n):
    t = [randint(-10000000, 100000000) for _ in range(n)]
    assert qsort(t) == sorted(t)


if __name__ == "__main__":
    seed(42)
    test_sort()
    speed(100000)
