comparisons = 0


def lt(a, b):
    global comparisons
    comparisons += 1
    return a < b


def gt(a, b):
    global comparisons
    comparisons += 1
    return a > b


def minmaxrec(t):
    if len(t) > 2:
        min1, max1 = minmaxrec(t[:2])
        min2, max2 = minmaxrec(t[2:])

        min = min2 if lt(min2, min1) else min1
        max = max2 if gt(max2, max1) else max1

        return min, max

    elif len(t) == 2:
        if gt(t[0], t[1]):
            return t[1], t[0]
        else:
            return t[0], t[1]

    else:
        return t[0], t[0]


def minmaxnaive(t):
    min = t[0]
    max = t[0]

    for i in t[1:]:
        if lt(i, min):
            min = i
        elif gt(i, max):
            max = i

    return min, max


from random import randint

t = [randint(-100000, 100000) for _ in range(1900)]
print("n =", len(t))
print("real min, max =", min(t), max(t))

comparisons = 0
print("min, max =", minmaxrec(t))
print("did", comparisons, "comparisons")

comparisons = 0
print("min, max =", minmaxnaive(t))
print("did", comparisons, "comparisons")
