from math import inf


def optimize_stops(t, L, S, P):
    """
    Go to 't' minimizing stops.
    At each station go to the farthest one.

    :param t: target
    :param L: tank capacity
    :param S: stations
    :param P: prices
    :return: path taken
    """
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
    """
    Find cheapest path to 't' always buying all fuel.

    :param t: target
    :param L: tank capacity
    :param S: stations
    :param P: prices
    :return: minimum cost needed to get to station i
    """
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


def optimize_cost_any_amount(t, L, S, P):
    """
    Find cheapest path to 't'. Can buy any amount of fuel.
    At each station find next station with cheapest fuel.
    If current station has cheapest fuel
    buy all fuel and go to next cheapest.

    :param t: target
    :param L: tank capacity
    :param S: stations
    :param P: prices
    :return: (money spent, path)
    """
    assert t > max(S)
    S = [0] + S + [t]
    P = [0] + P + [0]
    n = len(S)
    path = []

    pos = 0
    tank = L
    spent = 0

    while S[pos] < t:
        max_range = S[pos] + L

        # find station with cheapest fuel
        next_stop = pos + 1
        for i in range(pos + 1, n):
            if S[i] <= max_range:
                if P[i] < P[next_stop]:
                    next_stop = i
            else:
                break

        if P[next_stop] > P[pos]:
            # no station has cheaper fuel
            # buy all fuel here
            missing = max(0, L - tank)
            spent += missing * P[pos]
            tank = L

        else:
            # buy enough to get to next_stop
            missing = max(0, S[next_stop] - S[pos] - tank)
            spent += missing * P[pos]
            tank += missing

        if S[next_stop] > max_range:
            print("Stuck")
            break

        # burn fuel and go
        tank -= S[next_stop] - S[pos]
        pos = next_stop
        path.append(next_stop)

    return spent, path


S = [20, 30]
P = [1.5, 1.1]
t = 50
L = 40
print(optimize_stops(t, L, S, P))
print(optimize_cost(t, L, S, P))
print(optimize_cost_any_amount(t, L, S, P))
