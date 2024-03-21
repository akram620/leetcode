from typing import List


def min_cos_climbing_stairs(cost: List[int]) -> int:
    n = len(cost)
    if n == 2:
        return min(cost)

    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

    return min(dp[-1], dp[-2])


def min_cos_climbing_stairs1(cost: List[int]) -> int:
    if len(cost) == 2:
        return min(cost)
    if len(cost) == 3:
        return min(cost[1], cost[2])

    p1 = cost[1]
    p2 = cost[2] + min(cost[0], cost[1])

    for i in range(3, len(cost)):
        p1, p2 = p2, min(p1, p2) + cost[i]

    return min(p1, p2)


print(min_cos_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

print(min_cos_climbing_stairs1([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
