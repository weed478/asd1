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


if __name__ == "__main__":
    print(tanagram("kotomysz", "tokmysoz", 3))
    print(tanagram("kotomysz", "tokmysoz", 2))
