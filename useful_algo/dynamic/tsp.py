from math import sqrt, inf


class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return self.name

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
    C.sort(key=lambda c: c.x)
    n = len(C)

    def d(i, j):
        return C[i].distance(C[j])

    F = [[inf] * n for _ in range(n)]
    F[0][1] = d(0, 1)

    M = [None] * n

    def f(i, j):
        if F[i][j] != inf:
            return F[i][j]

        if i == j - 1:
            best = inf
            for k in range(j - 1):
                x = f(k, j - 1) + d(k, j)
                if x < best:
                    best = x
                    M[j] = k
            F[i][j] = best
        else:
            F[i][j] = f(i, j - 1) + d(j - 1, j)

        return F[i][j]

    solution = inf
    sol_i = None
    for i in range(1, n - 1):
        x = f(i, n - 1) + d(i, n - 1)
        if x < solution:
            solution = x
            sol_i = i

    print(solution)

    route_a = []
    route_b = []

    swapped = False
    i = sol_i

    for j in range(n - 1, 0, -1):
        if swapped:
            route_b.append(C[j])
        else:
            route_a.append(C[j])

        if i == j - 1:
            i = M[j]
            swapped = not swapped

    print(C[0], end=' ')
    for c in reversed(route_a):
        print(c, end=' ')
    for c in route_b:
        print(c, end=' ')
    print(C[0])


if __name__ == "__main__":
    C = [City("Wrocław", 0, 2),
         City("Warszawa", 4, 3),
         City("Gdańsk", 2, 4),
         City("Kraków", 3, 1)]

    D = [City("A", 0, 2),
         City("B", 1, 1),
         City("C", 4, 1),
         City("D", 5, 3),
         City("E", 6, 3),
         City("F", 8, 3),
         City("G", 7, 4),
         City("H", 2, 4),
         City("I", 0.5, 2.5),
         City("J", 1.5, 3.5)]
    D_sol = "A I J H D E G F C B A"
    D_num = 18.892922226

    E = [City("A", 0, 2),
         City("B", 4, 3),
         City("C", 2, 4),
         City("D", 3, 1),
         City("E", 1, 3),
         City("F", 0.5, -2)]
    E_sol = "A E C B D F A"
    E_num = 15.23681679184

    F = [City("A", 0, 0),
         City("B", 1, 1),
         City("C", 2, 0),
         City("D", 3, 1)]

    tsp(C)
    tspb(C)
