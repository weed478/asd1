class ArrView:
    def __init__(self, t, s=None, e=None):
        if s is None:
            s = 0
        elif s < 0:
            s = len(t) - 1 + s

        if e is None:
            e = len(t)
        elif e < 0:
            e = len(t) + e

        self.t = t
        self.s = s
        self.e = e

    def __repr__(self):
        s = "["
        for i in self[:-1]:
            s += repr(i) + ", "
        s += repr(self[len(self) - 1]) + "]"
        return s

    def __len__(self):
        return self.e - self.s

    def __eq__(self, other):
        if len(self) != len(other):
            return False

        for i in range(len(self)):
            if self[i] != other[i]:
                return False

        return True

    def __getitem__(self, i):
        if type(i) == int:
            if i < 0:
                i = len(self) - 1 + i
            return self.t[self.s + i]
        elif type(i) == slice:
            return ArrView(self, i.start, i.stop)

    def __setitem__(self, i, value):
        self.t[self.s + i] = value

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]


if __name__ == "__main__":
    t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("t:", t)

    tv = ArrView(t)
    print("tv:", tv)

    assert tv == t
    assert tv[2] == t[2]

    print(tv[2:5])
    assert tv[2:5] == t[2:5]

    tv = tv[2:5]
    assert tv[0] == t[2]

    print(tv[1:])
    assert tv[1:] == t[3:5]

