from queue import PriorityQueue


def count_chars(code, F):
    count = 0
    for i in range(len(F)):
        count += len(code[i]) * F[i]
    return count


def huffman(S, F):
    Q = PriorityQueue()

    for i in range(len(S)):
        Q.put((F[i], i))

    root = None

    while not Q.empty():
        f1, s1 = Q.get()

        if Q.empty():
            root = s1
            break

        f2, s2 = Q.get()

        s = (s1, s2)
        f = f1 + f2

        Q.put((f, s))

    code = ["" for _ in range(len(S))]

    def make_code(s, c):
        if type(s) is tuple:
            make_code(s[0], c + "0")
            make_code(s[1], c + "1")
        else:
            code[s] = c

    make_code(root, '')

    for i in range(len(S)):
        print(S[i], ": ", code[i], sep="")

    print("Length =", count_chars(code, F))


if __name__ == "__main__":
    S = ["a", "b", "c", "d", "e", "f"]
    F = [10, 11, 7, 13, 1, 20]
    huffman(S, F)
