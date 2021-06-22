from random import random


def bucket_sort(T, lo, hi, per_bucket):
    n = len(T)
    n_buckets = max(1, int(n / per_bucket))
    buckets = [[] for _ in range(n_buckets)]

    for i in T:
        bucket_i = min(int((i - lo) / ((hi - lo) / n_buckets)), n_buckets - 1)
        buckets[bucket_i].append(i)

    for b in buckets:
        b.sort()

    i = 0
    for b in buckets:
        for x in b:
            T[i] = x
            i += 1


if __name__ == "__main__":
    t = [random() for _ in range(100)]
    lo = min(t)
    hi = max(t)
    print(t)
    bucket_sort(t, lo, hi, 10)
    print(t)
