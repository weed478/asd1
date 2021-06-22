"""
Index tracking array
"""


class IndexArray:
    def __init__(self, n):
        self.ind2item = list(range(n))
        self.item2ind = list(range(n))

    def __len__(self):
        return len(self.ind2item)

    def __setitem__(self, key, value):
        self.ind2item[key] = value
        self.item2ind[value] = key

    def __getitem__(self, key):
        return self.ind2item[key]

    def index_of(self, item):
        return self.item2ind[item]
