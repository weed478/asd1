def lin_max(t):
    sum = 0
    max_sum = 0

    for x in t:
        sum += x

        if sum < 0:
            sum = 0

        max_sum = max(sum, max_sum)

    return max_sum


def round_max(t):
    n = len(t)
    start = 0
    length = 0
    sum = 0
    max_sum = 0

    start_moved = False

    while (not start_moved or start != 0) and length < n:
        sum += t[(start + length) % n]
        length += 1

        if sum < 0:
            sum = 0
            start += length
            length = 0
            start_moved = True

        max_sum = max(sum, max_sum)

    return max_sum


if __name__ == "__main__":
    T = [3, 1, -5, 4, -3, 1, -3, 6, -4, -2, 4]
    print(round_max(T))
