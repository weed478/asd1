from random import randrange


class Tank:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __repr__(self):
        return "({}, {}, {}, {})".format(self.x, self.y, self.w, self.h)


def rand_tank(x, y, w, h):
    x0 = randrange(x, x + w)
    y0 = randrange(y, y + h)
    x1 = randrange(x, x + w)
    y1 = randrange(y, y + h)

    x = min(x0, x1)
    y = min(y0, y1)
    w = abs(x0 - x1)
    h = abs(y0 - y1)

    return Tank(x, y, w, h)


def print_tanks(tanks, x, y):
    board = [[" " for _ in range(x)] for _ in range(y)]
    for t in tanks:
        for x in range(t.x, t.x + t.w):
            for y in range(t.y, t.y + t.h):
                board[y][x] = "#"

    for row in reversed(board):
        for f in row:
            print(f, "", end="")
        print()


def sorting(tanks, target):
    borders = []
    for t in tanks:
        borders.append((t.y, t.w))
        borders.append((t.y + t.h, -t.w))

    borders.sort(key=lambda x: x[0])

    last_y = borders[0][0]
    y = last_y
    width = borders[0][1]

    target_area = target
    area = 0
    for y, w in borders[1:]:
        dy = y - last_y
        last_y = y
        area += dy * width
        if area >= target_area:
            y += (target_area - area) / width
            break
        width += w

    return y


def tanks_under(tanks, h):
    count = 0
    for t in tanks:
        if t.y + t.h < h:
            count += 1
    return count


def bisection(tanks, target):
    h_top = max(map(lambda t: t.y + t.h, tanks))
    h_bottom = 0

    t_under_bottom = -1
    t_under_top = -2

    ops = 0

    while t_under_bottom != t_under_top:
        ops += 1

        h_mid = (h_top + h_bottom) / 2

        t_under_bottom = 0
        t_under_top = 0
        vol_under_mid = 0

        for t in tanks:
            top = t.y + t.h
            if top < h_bottom:
                t_under_bottom += 1
                t_under_top += 1

            elif top < h_top:
                t_under_top += 1

            vol_under_mid += t.w * (min(h_mid, t.y + t.h) - min(h_mid, t.y))

        if target < vol_under_mid:
            h_top = h_mid
        else:
            h_bottom = h_mid

    print(ops, "bisections")

    return t_under_bottom


'''
9         # #
8         # #
7  # # #          #
6  # # #    # #   #
5           # #   #
4       #   # #   # 
3       #         #
2   # #   # # #
1   # #   # # # # # 
0   # #         # #
  0 1 2 3 4 5 6 7 8 9
'''

# tanks = [
#     Tank(1, 0, 2, 3),
#     Tank(4, 1, 3, 2),
#     Tank(7, 0, 2, 2),
#     Tank(3, 3, 1, 2),
#     Tank(8, 3, 1, 5),
#     Tank(5, 4, 2, 3),
#     Tank(0, 6, 3, 2),
#     Tank(4, 8, 2, 2)
# ]

# print_tanks(tanks, 10, 10)

n = 100000
w = 2**256
t_vol = w * w / 2
tanks = [rand_tank(0, 0, w, w) for _ in range(n)]

print(tanks_under(tanks, sorting(tanks, t_vol)))
print(bisection(tanks, t_vol))
