"""
Do wyczerpania znaków:
- weż pierwsze wystąpienie znaku c = x[i]
- dopasuj do pierwszego wystąpienia c w y[i-t : i+t]
"""

from collections import deque


"""
Implementacja O(n*t)
"""
def tanagram(x, y, t):
    if len(x) != len(y):
        return False

    n = len(x)
    x_used = [False] * n
    y_used = [False] * n

    for xi in range(n):
        for yi in range(max(0, xi - t), min(xi + t + 1, n)):
            if not y_used[yi] and y[yi] == x[xi]:
                x_used[xi] = True
                y_used[yi] = True

    return False not in y_used and False not in x_used


def ord_i(c):
    return ord(c) - ord('a')


"""
O(n)
"""
def tanagram2(x, y, t):
    if len(x) != len(y):
        return False

    n = len(x)
    num_chars = ord('z') - ord('a') + 1

    # znalezione indeksy każdego znaku
    x_letter_pos = [deque() for _ in range(num_chars)]
    y_letter_pos = [deque() for _ in range(num_chars)]

    # po lewej stronie kolejki będą wcześniejsze wystąpienia
    for i in range(n):
        x_letter_pos[ord_i(x[i])].append(i)
        y_letter_pos[ord_i(y[i])].append(i)

    for ci in range(num_chars):
        # dopasuj wszystkie wystąpienia
        while len(x_letter_pos[ci]) > 0:
            if len(y_letter_pos[ci]) == 0:
                # nie ma do czego dopasować
                return False

            # weż pierwsze wystąpienia
            xi = x_letter_pos[ci].popleft()
            yi = y_letter_pos[ci].popleft()

            # jeśli pierwsze wystąpienie znaku w x nie da się dopasować do pierwszego wystąpienia w y
            # to znaczy, że znak w y nie można dopasować do żadnego innego znaku w x
            if abs(xi - yi) > t:
                return False

    return True


if __name__ == "__main__":
    print(tanagram("kotomysz", "tokmysoz", 3))
    print(tanagram2("kotomysz", "tokmysoz", 3))

    print(tanagram("kotomysz", "tokmysoz", 2))
    print(tanagram2("kotomysz", "tokmysoz", 2))
