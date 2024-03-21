def climb_stairs(n: int) -> int:
    if n < 3:
        return n

    dp = [0] * n
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]


def climb_stairs1(n: int) -> int:
    if n < 3:
        return n

    n1 = 1
    n2 = 2

    for i in range(2, n):
        n2, n1 = n2 + n1, n2

    return n2


print(climb_stairs(10))
