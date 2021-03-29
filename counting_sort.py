from random import randint


def counting_sort(A, min, max):
    k = max - min + 1
    C = [0] * k

    for x in A:
        C[x - min] += 1

    for i in range(1, k):
        C[i] += C[i - 1]

    B = [0] * len(A)
    for x in reversed(A):
        C[x] -= 1
        B[C[x]] = x

    return B


if __name__ == "__main__":
    T = [randint(0, 3) for _ in range(20)]
    print(T)
    print(counting_sort(T, min(T), max(T)))
