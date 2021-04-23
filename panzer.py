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
    pass


S = [10, 20]
P = [0, 0]
t = 24
L = 15
print(optimize_stops(t, L, S, P))
