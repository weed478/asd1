from math import inf


class Block:
    def __init__(self, i, k):
        self.i = i
        self.a = k[0]
        self.b = k[1]
        self.h = k[2]
        self.span = (self.a, self.b)
        self.top = self.h


class Node:
    def __init__(self, value):
        self.value = value
        self.span = (-inf, inf)

        self.parent = None
        self.left = None
        self.right = None


class Leaf:
    def __init__(self, span, parent):
        self.span = span
        self.parent = parent
        self.h = 0


def insert_node(T, node):
    if node.value < T.value:
        node.span = (node.span[0], T.value)
        if T.left is None:
            T.left = node
            node.parent = T
        else:
            insert_node(T.left, node)

    if T.value < node.value:
        node.span = (T.value, node.span[1])
        if T.right is None:
            T.right = node
            node.parent = T
        else:
            insert_node(T.right, node)


def insert_leafs(T, span):
    if T.left is None:
        T.left = Leaf((span[0], T.value), T)
    else:
        insert_leafs(T.left, (span[0], T.value))

    if T.right is None:
        T.right = Leaf((T.value, span[1]), T)
    else:
        insert_leafs(T.right, (T.value, span[1]))


def make_tree(K):
    root = Node(K[0].a)
    insert_node(root, Node(K[0].b))

    for k in K[1:]:
        insert_node(root, Node(k.a))
        insert_node(root, Node(k.b))

    insert_leafs(root, (-inf, inf))

    return root


def contains(o, i):
    return o[0] <= i[0] and i[1] <= o[1]


def insert_block(T, k):
    if type(T) == Leaf:
        if contains(k.span, T.span):
            T.h = max(T.h + k.h, k.top)
            k.top = T.h

    else:
        assert T.left is not None and T.right is not None
        insert_block(T.left, k)
        insert_block(T.right, k)


def blocks_height(K):
    T = make_tree(K)
    for k in K:
        insert_block(T, k)
    for k in K:
        print("{}: {}".format(k.i, k.top))
    return max(K, key=lambda k: k.top).top


if __name__ == "__main__":
    K = [(1, 3, 1), (2, 5, 2), (0, 3, 2), (8, 9, 3), (4, 6, 1)]
    K = list(map(lambda i: Block(i[0], i[1]), enumerate(K)))
    print(blocks_height(K))
