def longest_incomplete(A, k):
    n = len(A)

    # O(nlogn), trzebaby BST i byłoby nlogk
    numbers = []
    for x in sorted(A):
        if len(numbers) < 1 or numbers[-1] != x:
            numbers.append(x)

    # O(logk)
    def find_number(x):
        def _find_number(beg, end):
            mid = (beg + end) // 2
            if x < numbers[mid]:
                return _find_number(beg, mid - 1)
            elif numbers[mid] < x:
                return _find_number(mid + 1, end)
            else:
                return mid
        i = _find_number(0, k - 1)
        assert numbers[i] == x
        return i

    beg = 0
    end = -1
    best_l = 0

    used = [0] * k
    n_used = 0

    # O(nlogk)
    while end < n - 1:
        end += 1
        # O(logk)
        num_i = find_number(A[end])

        if used[num_i] == 0:
            n_used += 1
        used[num_i] += 1

        while n_used >= k:
            assert used[find_number(A[beg])]
            # O(logk)
            used[find_number(A[beg])] -= 1
            if used[find_number(A[beg])] == 0:
                n_used -= 1
            beg += 1

        best_l = max(best_l, end - beg + 1)

    return best_l


if __name__ == "__main__":
    print(longest_incomplete([1, 100, 5, 100, 1, 5, 1, 5], 3))  # 4
