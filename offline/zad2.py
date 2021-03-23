from random import randint, seed


class Node:
    def __init__(self):
        self.next = None
        self.value = None


def partition(first):
    """
    Split into less than, equal, greater than
    and return pointer to end of equal elements
    """
    lt = None
    eq = None
    gt = None

    p = first.next

    # put first element into equal list
    first.next = eq
    eq = first

    while p is not None:
        q = p
        p = p.next

        if q.value < eq.value:
            q.next = lt
            lt = q
        elif q.value > eq.value:
            q.next = gt
            gt = q
        else:
            q.next = eq
            eq = q

    # "first" is the last equal element
    return lt, eq, first, gt


def _qsort(first):
    if first is None:
        return first, first

    lt, eq, eq_e, gt = partition(first)

    lt, lt_e = _qsort(lt)
    gt, gt_e = _qsort(gt)

    # join non null lists
    if lt is None:
        if gt is None:
            return eq, eq_e
        else:
            eq_e.next = gt
            return eq, gt_e
    else:
        lt_e.next = eq
        if gt is None:
            return lt, eq_e
        else:
            eq_e.next = gt
            return lt, gt_e


def qsort(L):
    return _qsort(L)[0]


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")


seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]
L = tab2list(T)

print("przed sortowaniem: L =", end=" ")
printlist(L)
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
    print("List jest pusta, a nie powinna!")
    exit(0)

P = L
while P.next != None:
    if P.value > P.next.value:
        print("Błąd sortowania")
        exit(0)
    P = P.next

print("OK")
