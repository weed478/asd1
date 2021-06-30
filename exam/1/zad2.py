"""
Jakub Karbowski

Definiujemy stan robota krotką (x, y, rotation, speed).
Niech to będą wierzchołki w grafie.
Dla każdego stanu dodajemy możliwe przejścia do innych stanów.
Dijkstrą liczymy odległości od stanu początkowego.


Złożoność:
Generacja grafu: O(w * h)  # width, height planszy
Dijkstra na adj list: O(ElogV); ile to E a ile V?
V = ilość stanów = w * h * N_ROTS * N_SPEEDS
E <= V^2 na pewno.
Ale jest lepiej.
Z każdego stanu możemy przejść do najwyżej 3 innych (forward, left, right).
Czyli krawędzi będzie najwyżej 3V.

Finalna złożoność: O(w*h*log(w*h))


Pamięć:
Przechowujemy różne rzeczy dla każdego stanu, więc mamy O(w*h)
"""


from zad2testy import runtests
from math import inf, isinf
from queue import PriorityQueue


N_SPEEDS = 3
TOP_SPEED = 2
N_ROTS = 4


def accelerate(s):
    return min(TOP_SPEED, s + 1)


ROT_COST = 45

MOVE_COST = [  # MOVE_COST[s] = ...
    60,
    40,
    30
]


def robot(L, A, B):
    h = len(L)  # height
    w = len(L[0])  # width

    """
    stan robota to:
    x
    y
    r - rotation (0, 1, 2, 3)
    s - speed (0, 1, 2)
    """

    """
    plansza ma X w prawo, Y w dół
    """

    # adj list
    G = [[[[[] for s in range(N_SPEEDS)] for r in range(N_ROTS)] for y in range(h)] for x in range(w)]

    # generujemy możliwe ruchy
    for x in range(w):
        for y in range(h):
            # tych pętli nie wliczamy do złożoniści bo mają stałą długość
            for r in range(N_ROTS):
                for s in range(N_SPEEDS):
                    # prawo
                    if r == 0:
                        # wykrywanie kolizji
                        if x + 1 < w and L[y][x + 1] != 'X':
                            # do przodu rozpędzając się
                            G[x][y][r][s].append(((x + 1, y, r, accelerate(s)), MOVE_COST[s]))
                            #                     |  x  | y |r|       s       |     time    |

                        # zakręty
                        G[x][y][r][s].append(((x, y, 1, 0), ROT_COST))
                        G[x][y][r][s].append(((x, y, 3, 0), ROT_COST))

                    # góra
                    if r == 1:
                        if 0 <= y - 1 and L[y - 1][x] != 'X':
                            G[x][y][r][s].append(((x, y - 1, r, accelerate(s)), MOVE_COST[s]))
                        G[x][y][r][s].append(((x, y, 0, 0), ROT_COST))
                        G[x][y][r][s].append(((x, y, 2, 0), ROT_COST))

                    # lewo
                    if r == 2:
                        if 0 <= x - 1 and L[y][x - 1] != 'X':
                            G[x][y][r][s].append(((x - 1, y, r, accelerate(s)), MOVE_COST[s]))
                        G[x][y][r][s].append(((x, y, 1, 0), ROT_COST))
                        G[x][y][r][s].append(((x, y, 3, 0), ROT_COST))

                    # dół
                    if r == 3:
                        if y + 1 < h and L[y + 1][x] != 'X':
                            G[x][y][r][s].append(((x, y + 1, r, accelerate(s)), MOVE_COST[s]))
                        G[x][y][r][s].append(((x, y, 2, 0), ROT_COST))
                        G[x][y][r][s].append(((x, y, 0, 0), ROT_COST))

    # dijkstra

    # odległość każdego stanu
    d = [[[[inf for s in range(N_SPEEDS)] for r in range(N_ROTS)] for y in range(h)] for x in range(w)]
    visited = [[[[False for s in range(N_SPEEDS)] for r in range(N_ROTS)] for y in range(h)] for x in range(w)]
    Q = PriorityQueue()

    d[A[0]][A[1]][0][0] = 0
    Q.put((0, (A[0], A[1], 0, 0)))

    while not Q.empty():
        _, state = Q.get()
        x, y, r, s = state

        if visited[x][y][r][s]:
            continue
        visited[x][y][r][s] = True

        for (new_state, cost) in G[x][y][r][s]:
            nx, ny, nr, ns = new_state
            if d[x][y][r][s] + cost < d[nx][ny][nr][ns]:
                d[nx][ny][nr][ns] = d[x][y][r][s] + cost
                Q.put((d[nx][ny][nr][ns], (nx, ny, nr, ns)))

    best_cost = inf
    for r in range(N_ROTS):
        for s in range(N_SPEEDS):
            best_cost = min(best_cost, d[B[0]][B[1]][r][s])

    return None if isinf(best_cost) else best_cost


runtests(robot)
