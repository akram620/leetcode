from typing import List


def min_cos_climbing_stairs(cost: List[int]) -> int:
    if len(cost) == 2:
        return min(cost)
    if len(cost) == 3:
        return min(cost[1], cost[2])

    p1 = cost[1]
    p2 = cost[2] + min(cost[0], cost[1])

    for i in range(3, len(cost)):
        p1, p2 = p2, min(p1, p2) + cost[i]

    return min(p1, p2)


print(min_cos_climbing_stairs([0, 0, 0, 1]))
