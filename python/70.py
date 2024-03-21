def climb_stairs(n: int) -> int:
    if n < 3:
        return n

    n1 = 1
    n2 = 2

    for i in range(2, n):
        n2, n1 = n2 + n1, n2

    return n2


print(climb_stairs(10))
