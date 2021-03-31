from random import randint, seed


def merge(t1, s1, e1, t2, s2, e2, tout, s3, e3):
    i1 = s1
    i2 = s2
    for i in range(s3, e3):
        if i2 >= e2 or (i1 < e1 and t1[i1] <= t2[i2]):
            tout[i] = t1[i1]
            i1 += 1

        else:
            tout[i] = t2[i2]
            i2 += 1


def _mergesort(t, buf, s, e):
    if e - s < 2:
        return

    mid = (s + e) // 2

    _mergesort(buf, t, s, mid)
    _mergesort(buf, t, mid, e)

    merge(buf, s, mid, buf, mid, e, t, s, e)


def mergesort(T):
    buf = T.copy()
    _mergesort(T, buf, 0, len(T))
    return T


seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]

print("przed sortowaniem: T =", T)
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T) - 1):
    if T[i] > T[i + 1]:
        print("Błąd sortowania!")
        exit()

print("OK")
