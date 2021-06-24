from math import inf
from zad2testy import runtests


class Node:
    def __init__(self):
        self.left = None
        self.leftval = 0

        self.right = None
        self.rightval = 0

        self.X = None


def set_left(node, target, val):
    node.left = target
    node.leftval = val


def set_right(node, target, val):
    node.right = target
    node.rightval = val


cache_k = 0


class Cache:
    def __init__(self):
        global cache_k
        self.f = [None] * (cache_k + 1)
        self.g = None


def f(T, k):
    if k == 0:
        return 0

    if T is None:
        return -inf

    if T.X is None:
        T.X = Cache()

    if T.X.f[k] is not None:
        return T.X.f[k]

    best = -inf

    if T.right is not None:
        best = max(best, T.rightval + f(T.right, k - 1))

    if T.left is not None:
        best = max(best, T.leftval + f(T.left, k - 1))

    if None not in [T.left, T.right] and k >= 2:
        best = max(best,
                   max(map(lambda i:
                           T.leftval + f(T.left, i - 1) + T.rightval + f(T.right, k - i - 1)
                           , range(1, k))
                       ))

    T.X.f[k] = best
    return best


def g(T, k):
    if k == 0:
        return 0

    if T is None:
        return -inf

    if T.X is None:
        T.X = Cache()

    if T.X.g is not None:
        return T.X.g

    best = max(
        g(T.left, k),
        g(T.right, k),
        f(T, k)
    )

    T.X.g = best
    return best


def valuable_tree(T, k):
    global cache_k
    cache_k = k
    return g(T, k)


if __name__ == "__main__":
    A = Node()
    B = Node()
    C = Node()
    D = Node()
    E = Node()
    F = Node()
    G = Node()

    set_left(A, B, 1)
    set_right(A, E, 5)

    set_left(B, D, 6)
    set_right(B, C, 2)

    set_left(C, F, 8)
    set_right(C, G, 10)

    print(valuable_tree(A, 3))

    runtests(valuable_tree)
