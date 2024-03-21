from typing import List


def max_sub_array(nums: List[int]) -> int:
    n = len(nums)
    if n < 2:
        return nums[0]

    s = nums[0]
    m = nums[0]

    for i in range(1, n):
        s = max(nums[i], s + nums[i])
        m = max(m, s)

    return m


print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
