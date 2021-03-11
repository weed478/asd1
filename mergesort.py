from random import seed, randint
from arr_view import ArrView


def merge(t1, t2, tout):
    n1 = len(t1)
    n2 = len(t2)
    n = len(tout)

    assert n1 + n2 == n

    i1 = 0
    i2 = 0
    for i in range(n):
        if i2 >= n2 or (i1 < n1 and t1[i1] <= t2[i2]):
            tout[i] = t1[i1]
            i1 += 1

        else:
            tout[i] = t2[i2]
            i2 += 1


def _mergesort(t, buf):
    assert len(t) == len(buf)
    assert t == buf

    n = len(t)

    if n < 2:
        return

    mid = n // 2

    _mergesort(buf[:mid], t[:mid])
    _mergesort(buf[mid:], t[mid:])

    merge(buf[0:mid], buf[mid:n], t)


def mergesort(t):
    t = t.copy()
    buf = t.copy()
    _mergesort(ArrView(t), ArrView(buf))
    return t


def tests():
    assert mergesort([1]) == [1]
    assert mergesort([1, 2]) == [1, 2]
    assert mergesort([2, 1]) == [1, 2]
    assert mergesort([2, 1, 3]) == [1, 2, 3]
    t = [randint(0, 9) for _ in range(10)]
    assert mergesort(t) == sorted(t)
    print("Pass")


seed(42)
tests()
