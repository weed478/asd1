class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        s = "["
        p = self
        while True:
            s += repr(p.value)
            if p.next is None:
                s += "]"
                break
            else:
                s += ", "
            p = p.next
        return s


def tab2list(t):
    w = None
    for x in reversed(t):
        w = Node(x, w)
    return w
