def solve(l1, l2):
    l1.append(float('inf'))
    l2.append(float('inf'))
    n1, n2 = 0, 0
    res = []

    while l1[n1] != float('inf') or l2[n2] != float('inf'):
        if l1[n1] <= l2[n2]:
            res.append(l1[n1])
            n1 += 1
        else:
            res.append(l2[n2])
            n2 += 1
    l1.pop(), l2.pop()
    return res


if __name__ == '__main__':
    print(solve([-2, 0, 3, 6], [-1, 0, 5, 5, 8]))