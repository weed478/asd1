from random import randint
from zad1testy import runtests


"""
Klasa pozwala indeksowanie po strukturze wyglądającej jak tablica 1D n^2 elementów:
|     A      |   B   |      C       |

A w tle działa na tablicy 2D NxN:
+---------------+
|       B'      |
+-------+-------+
|       |       |
|   A'  |   C'  |
|       |       |
|       |       |
+-------+-------+
Bądź w przypadku nieparzystego n:
+---------------+
|       B'      |
+---------------+
|       A'      |
|               |
+---------------+
|       C'      |
|               |
+---------------+

Obszary A, B, C są mapowane na A', B', C' 

len(B) = n
len(A) = len(C) = (n^2 - n) / 2

"""
class InterpretLayer1:
    def __init__(self, t):
        self.t = t
        self.n = len(t)

    def __len__(self):
        return len(self.t) * len(self.t)

    def __getitem__(self, i):
        i = self.get_index(i)
        return self.t[i[0]][i[1]]

    def __setitem__(self, i, v):
        i = self.get_index(i)
        self.t[i[0]][i[1]] = v

    def get_index(self, i):
        n = self.n

        if i < (n * n - n) // 2:
            if n % 2 == 1:
                return 1 + i // n, i % n
            else:
                return 1 + i // (n // 2), i % (n // 2)

        elif i < (n * n - n) // 2 + n:
            return 0, i - (n * n - n) // 2

        else:
            i -= (n * n - n) // 2 + n
            if n % 2 == 1:
                return n // 2 + 1 + i // n, i % n
            else:
                return 1 + i // (n // 2), n // 2 + i % (n // 2)


"""
Klasa pozwala na indeksowanie po strukturze tablicy 2D NxN:
+---------------+
|       B'      |
+-------+-------+
|       |       |
|   A'  |   C'  |
|       |       |
|       |       |
+-------+-------+
Bądź w przypadku nieparzystego n:
+---------------+
|       B'      |
+---------------+
|       A'      |
|               |
+---------------+
|       C'      |
|               |
+---------------+

Mapując obszary A', B', C' do A'', B'', C'':
+---+-----------+
|B''|           |
+---+---+  C''  |
|   |B''|       |
|   +---+---+   |
|       |B''|   |
|  A''  +---+---+
|           |B''|
+-----------+---+
"""
class InterpretLayer2:
    def __init__(self, t):
        self.t = t
        self.n = len(t)

    def __len__(self):
        return len(self.t)

    def __getitem__(self, y):
        class _Row:
            def __init__(self, owner):
                self.owner = owner

            def __getitem__(self, x):
                i = self.owner.get_index(y, x)
                return self.owner.t[i[0]][i[1]]

            def __setitem__(self, x, v):
                i = self.owner.get_index(y, x)
                self.owner.t[i[0]][i[1]] = v

        return _Row(self)

    def get_index(self, y, x):
        n = self.n

        if y == 0:
            return x, x

        diag = y + (n - 1 - x)

        if n % 2 == 0:
            if (diag > n - 1 and x < n // 2) or \
               (diag < n - 1 and x >= n // 2):
                return y, x

            if x < n // 2:
                return n - y, n - 1 - x

            if diag == n - 1:
                return 0, x

            return n - 1 - y, n - 1 - x

        else:
            if (diag > n - 1 and y < n // 2 + 1) or \
               (diag < n - 1 and y > n // 2):
                return y, x

            if y < n // 2 + 1:
                return n - y, n - 1 - x

            if diag == n - 1:
                return n // 2, x

            return n - 1 - y, n - 1 - x


def partition(A, p, r):
    i = p - 1

    for j in range(p, r):
        if A[j] <= A[r - 1]:
            i += 1
            A[i], A[j] = A[j], A[i]

    return i


def select(A, p, r, k):
    while r - p > 1:
        # zakładamy optymalny pivot
        q = partition(A, p, r)
        # less or equal | q | greater

        if k < q:
            r = q
        elif q < k:
            p = q + 1
        else:
            return q

    return p


def Median(T):
    n = len(T)
    
    """
    t jest widoczna jako tablica 1D długości n^2
    dzielimy na obszary:
    |        A        | B |       C       |
                      i   j
    
    B to przekątna, A dolny trójkąt, C górny trójkąt
    selectujemy elementy 'i' i 'j' dzieląc elementy na mniejsze, równe przekątnej,
    samą przekątną oraz wieksze, równe przekątnej    
    
    Dzięki klasom Interpret obszary A, B, C odpowiadają A'', B'', C''
    które są odpowiednio dolnym trójkątem, przekątną i górnym trójkątem
    Co kończy zadanie
    """
    t = InterpretLayer1(InterpretLayer2(T))
    N = len(t)

    select(t, 0, N, (n * n - n) // 2)
    select(t, (n * n - n) // 2, N, (n * n - n) // 2 + n - 1)


# runtests(Median)


def custom_tests():
    # t = [[1,   2,  3,  4,  5],
    #      [6,   7,  8,  9, 10],
    #      [11, 12, 13, 14, 15],
    #      [16, 17, 18, 19, 20],
    #      [21, 22, 23, 24, 25]]

    # t = [[1,  15, 11, 16],
    #      [5,  2,  7,  8],
    #      [9,  10, 3,  12],
    #      [13, 14, 6,  4]]

    # t = [[ 0,  1,  -1,  1,  0],
    #      [-1,  0,  1,  1,  -1],
    #      [-1, -1,  1,  -1,  1],
    #      [-1, 1, -1,  0,  1],
    #      [0, 1, 1, -1,  -1]]

    # t = [[1,  24, 23, 22, 21],
    #      [6,  2,  18, 17, 16],
    #      [11, 12, 3,  19, 25],
    #      [15, 14, 13, 4,  20],
    #      [10, 9,  8,  7,  5]]

    n = 21
    t = [[randint(-2, 2) for _ in range(n)] for _ in range(n)]

    n = len(t)
    T = InterpretLayer1(InterpretLayer2(t))
    N = len(T)

    select(T, 0, N, (n * n - n) // 2)
    select(T, (n * n - n) // 2, N, (n * n + n) // 2 - 1)

    for y in range(len(t)):
        for x in range(len(t)):
            print(t[y][x], end="\t")
        print()


custom_tests()
