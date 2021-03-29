from simple_node import Node, tab2list
from random import randint


def count(p):
    n = 0
    while p is not None:
        n += 1
        p = p.next
    return n


def insert_into_bucket(b, node):
    p = b
    q = b.next
    while q is not None and q.value > node.value:
        p = q
        q = q.next

    node.next = q
    p.next = node


def bucket_sort(wart):
    n = count(wart.next)
    buckets = [Node(None) for _ in range(n)]

    while wart.next is not None:
        p = wart.next
        wart.next = p.next

        bucket_i = p.value * n // 10

        insert_into_bucket(buckets[bucket_i], p)

    for b in reversed(buckets):
        while b.next is not None:
            p = b.next
            b.next = p.next
            p.next = wart.next
            wart.next = p


if __name__ == "__main__":
    t = [randint(0, 9) for _ in range(50)]
    print(t)
    l = Node(None, tab2list(t))
    bucket_sort(l)
    print(l.next)
