def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def MinHeap(t):
    return Heap(t, lambda a, b: a < b)


def MaxHeap(t):
    return Heap(t, lambda a, b: a > b)


class Heap:
    def __init__(self, t, cmp):
        self.t = t
        self.n = 0
        self.cmp = cmp

    def __getitem__(self, item):
        return self.t[item]

    def __setitem__(self, key, value):
        self.t[key] = value

    def __len__(self):
        return self.n

    def __repr__(self):
        return repr(self.t)

    def print(self, i=0, d=0):
        if i >= len(self):
            return

        print(" " * d + "- ", end="")
        print(self.t[i], ":", sep="")

        self.print(left(i), d + 1)
        self.print(right(i), d + 1)

    def swap(self, i, j):
        self[i], self[j] = self[j], self[i]

    def heapify(self, i=0):
        while True:
            m = i
            l = left(m)
            r = right(m)

            if l < len(self) and self.cmp(self[l], self[m]):
                m = l

            if r < len(self) and self.cmp(self[r], self[m]):
                m = r

            if m != i:
                self.swap(i, m)
                i = m
            else:
                break

    def build(self):
        self.n = len(self.t)
        for i in range(parent(len(self) - 1), -1, -1):
            self.heapify(i)

    def extract_top(self):
        max = self[0]
        self[0] = self[len(self) - 1]
        self.n -= 1
        self.heapify(0)
        return max

    def insert(self, k):
        self.n += 1

        i = len(self) - 1
        self[i] = k

        while parent(i) >= 0 and self.cmp(self[i], self[parent(i)]):
            self.swap(i, parent(i))
            i = parent(i)

    def increase_key(self, i, k):
        self[i] = k
        while parent(i) >= 0 and self.cmp(self[i], self[parent(i)]):
            self.swap(i, parent(i))
            i = parent(i)

    def sort(self):
        while len(self) > 0:
            self[len(self)] = self.extract_top()


if __name__ == "__main__":
    t = [5, 3, 4, 1, 2, 8, 7, 9, 6, 0]

    h = MinHeap(t)
    h.build()
    print(t)

    h.increase_key(5, -1)
    print(t)
