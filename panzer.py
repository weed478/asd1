from math import inf


def optimize_stops(t, L, S, P):
    S = [0] + S
    path = []

    pos = 0
    tank = L

    while S[pos] < t:
        max_range = tank

        if S[pos] + max_range >= t:
            break

        next_stop = -1
        for si in range(pos + 1, len(S)):
            if S[pos] + max_range >= S[si]:
                next_stop = si
            else:
                break

        if next_stop < 0:
            print("Paliwo było i nie ma")
            break

        pos = next_stop
        tank = L
        path.append(next_stop - 1)

    return path


def optimize_cost(t, L, S, P):
    assert t > max(S)
    S = [0] + S + [t]
    P = [0] + P + [0]

    n = len(S)
    F = [inf] * n

    """
    F[i] = min cost needed to get to station i and fill up
    F[0] = 0, tank starts at station 0
    F[i] = min { j, 0<=j<i } ( F[j] + P[i] * (S[i] - S[j]), S[i] - S[j] <= L )
    """

    F[0] = 0
    for i in range(1, n):
        for j in range(i):
            if S[i] - S[j] <= L:
                F[i] = min(F[i], F[j] + P[i] * (S[i] - S[j]))

    return F


S = [20, 30]
P = [1.5, 1.1]
t = 50
L = 40
print(optimize_cost(t, L, S, P))
