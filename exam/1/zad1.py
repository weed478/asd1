"""
Jakub Karbowski

Do każdego elementu dołączamy jego orginalny indeks; element to krotka (value; original index).
Puszczamy zwykły insertion sort (dobry do k-chaotycznych tablic).
Insertion sort będzie sobie przekładał elementy aż skończy.
Na końcu sprawdzamy o ile każdy element się przesunął i liczymy największe przesunięcie, które jest naszym k.

Złożoność:
Zwykły insertion sort O(n^2) ale mamy tablicę k-chaotyczną.
Dlatego złożoność wynosi O(nk); wewnętrzna pętla sorta wykona się max k razy.

Pamięciowo zajmujemy dodatkowo O(n).


---
Myślałem czy coś może nie heap ale ponieważ nie znamy k, trzebaby na początku wszystko do niego wrzucić,
co by potem zrobiło O(nlogn) zamiast O(nlogk).
"""


from zad1testy import runtests


def insertion_sort(A, p, r):
    for i in range(p + 1, r):
        for j in range(i, p, -1):
            if A[j - 1][0] > A[j][0]:
                A[j - 1], A[j] = A[j], A[j - 1]
            else:
                break


def chaos_index(T):
    n = len(T)

    A = [(T[i], i) for i in range(n)]

    insertion_sort(A, 0, n)

    k = 0
    for i in range(n):
        k = max(k, abs(A[i][1] - i))

    return k


runtests(chaos_index)
