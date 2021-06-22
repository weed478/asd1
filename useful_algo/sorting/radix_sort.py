from random import randint


def sort_by_digit(A, B, digit_mask):
    C = [0] * 10

    had_digit = False

    for x in A:
        C[(x // digit_mask) % 10] += 1
        if x >= digit_mask:
            had_digit = True

    for i in range(1, 10):
        C[i] += C[i - 1]

    for x in reversed(A):
        C[(x // digit_mask) % 10] -= 1
        B[C[(x // digit_mask) % 10]] = x

    return had_digit


def radix_sort(A):
    digit_mask = 1
    had_digit = True

    bufs = [A, [0] * len(A)]
    buf = 0

    while had_digit:
        had_digit = sort_by_digit(bufs[buf], bufs[buf ^ 1], digit_mask)
        buf ^= 1
        digit_mask *= 10

    return bufs[buf]


if __name__ == "__main__":
    T = [randint(0, 9999) for _ in range(20)]
    print(T)
    print(radix_sort(T))
