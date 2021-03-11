class ArrView:
    def __init__(self, t, s, e):
        self.t = t
        self.s = s
        self.e = e

    def __repr__(self):
        return repr(self.t[self.s:self.e])

    def __len__(self):
        return self.e - self.s

    def __eq__(self, other):
        return self.t[self.s:self.e] == other

    def __getitem__(self, i):
        if type(i) == int:
            return self.t[self.s + i]
        elif type(i) == slice:
            return ArrView(self.t, self.s + i.start, self.s + i.stop)

    def __setitem__(self, i, value):
        self.t[self.s + i] = value


if __name__ == "__main__":
    t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("t:", t)

    tv = ArrView(t, 2, 7)
    print("tv:", tv)

    print("tv[1]:", tv[1])
    assert t[3] == tv[1]

    print("tv[1:4]:", tv[1:4])
    assert tv[1:4] == t[3:6]
