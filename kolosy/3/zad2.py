"""
Jakub Karbowski

Zbyt piękne, żeby było prawdziwe.

Założenia:
- nie ucinamy korzenia
- nie ucinamy liści

Dla każdego węzła 'i' żeby odciąć jego parent od liści możemy
albo uciąć drzewo na poziomie 'i' albo poniżej węzła 'i' po stronach obu dzieci.

Wykonujemy akcję, która doda mniej do sumy uciętych wierzchołków
czyli min { utnij 'i', utnij pod 'i' po lewej + utnij pod 'i' po prawej }

Złożoność:
n - ilość węzłów
O(n)

Pamięć trochę problematyczna, bo rekurencja zajmuje
O(log n) w przypadku zbalansowanego drzewa
albo O(n) w najgorszym przypadku

"""

from zad2testy import runtests
from math import inf


class BNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def is_leaf(node):
    return node.left is node.right is None


def cutthetree(T):
    def cut(node):
        if node is None:
            return 0

        if is_leaf(node):
            return inf  # nie ucinamy lisci

        return min(node.value, cut(node.left) + cut(node.right))

    return cut(T.left) + cut(T.right)


runtests(cutthetree)
