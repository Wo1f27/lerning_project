def climbStairs(n: int) -> int:
    res = [1, 1]
    if n == 0 or n == 1:
        return 1

    for i in range(2, n + 1):
        res.append((res[i - 1]) + (res[i - 2]))
    return res[-1]



if __name__ == '__main__':
    print(climbStairs(6))
    print(climbStairs(12))
    print(climbStairs(-12))
    print(climbStairs(1))