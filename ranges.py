from random import randrange, shuffle


def random_interval():
    a = randrange(0, 1000000) / 10000
    b = randrange(0, 1000000) / 10000
    return min(a, b), max(a, b)


def contains(a, b):
    return a[0] < b[0] and b[1] < a[1]


def naive(ranges):
    ops = 0
    max_count = 0
    max_ri = 0
    for ri in range(len(ranges)):
        count = 0
        for r in ranges:
            ops += 1
            if contains(ranges[ri], r):
                count += 1

        if count > max_count:
            max_count = count
            max_ri = ri

    return ops  # max_ri


def sorting(ranges):
    ops = 0

    ranges = sorted(ranges, key=lambda r: r[1] - r[0], reverse=True)

    max_count = 0
    max_ri = 0

    for ri1 in range(len(ranges)):
        count = 0
        for ri2 in range(ri1 + 1, len(ranges)):
            ops += 1
            if contains(ranges[ri1], ranges[ri2]):
                count += 1

        if count > max_count:
            max_count = count
            max_ri = ri1

    return ops  # max_ri


def divconq(ranges):
    ops = 0
    ranges.sort(key=lambda r: abs(r[1] - r[0]), reverse=True)
    counts = [-1] * len(ranges)

    def _contained(ri):
        nonlocal ops
        if counts[ri] < 0:
            counts[ri] = 0
            for i in range(ri + 1, len(ranges)):
                ops += 1
                if contains(ranges[ri], ranges[i]):
                    counts[ri] += 1
        return counts[ri]

    [_contained(i) for i in range(len(ranges))]
    return ops


'''
 1 1.2 1.5 2 2.5 3 3.5 4 4.5 5 5.5 6 7 8 9 10
 |_________|  |  |_____|  |  |_____| |_| |_|
    |   |     |___________|     |
    |   |___________|           |
    |___________________________|
'''
# ranges = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (1.5, 3.5), (2.5, 4.5), (1.2, 5.5)]
# shuffle(ranges)

# print(ranges[naive(ranges)])
# print(sorting(ranges))

for n in range(100, 10000, 1000):
    ranges = [random_interval() for _ in range(n)]
    n_ops = naive(ranges)
    sort_ops = sorting(ranges)
    print("{}\t{}\t{}".format(n, n_ops, sort_ops))


