from math import sqrt


class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def distance(self, c):
        return sqrt((self.x - c.x) ** 2 + (self.y - c.y) ** 2)


def tsp(C):
    n = len(C)

    def d(i, j):
        return C[i].distance(C[j])

    def f(notX, i):
        try:
            return min((
                f(notX + [i], j) + d(j, i)
                for j in filter(lambda j:
                                j != i and j not in notX,
                                range(1, n))))
        except ValueError:
            return d(0, i)

    solution = min((f([], i) + d(i, 0) for i in range(1, n)))
    print(solution)


def tspb(C):
    n = len(C)

    def d(i, j):
        return C[i].distance(C[j])

    def f(i, j):
        if i == 0 and j == 1:
            return d(0, 1)

        if i == j - 1:
            return min((f(k, j - 1) + d(k, j) for k in range(j - 1)))
        else:
            return f(i, j - 1) + d(j - 1, j)

    solution = min((f(i, n - 1) + d(i, n - 1) for i in range(1, n - 1)))
    print(solution)


C = [City("Wrocław", 0, 2),
     City("Warszawa", 4, 3),
     City("Gdańsk", 2, 4),
     City("Kraków", 3, 1)]

tsp(C)
tspb(C)
