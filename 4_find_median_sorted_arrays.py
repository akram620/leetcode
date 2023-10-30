import math
from typing import List


# level: hard
def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) == 0 and len(nums2) == 1:
        return nums2[0] / 2

    if len(nums2) == 0 and len(nums1) == 1:
        return nums1[0] / 2

    p_1 = 0
    p_2 = 0

    res = []
    if len(nums1) == 0:
        res = nums2
    elif len(nums2) == 0:
        res = nums1
    else:
        while p_1 < len(nums1) and p_2 < len(nums2):

            if len(nums1) == 0:
                p_1 = -1
            if len(nums2) == 0:
                p_2 = -1

            if p_1 == -1:
                res.append(nums2[p_2])
                p_2 += 1
                continue
            if p_2 == -1:
                res.append(nums1[p_1])
                p_1 += 1
                continue

            if nums1[p_1] < nums2[p_2]:
                res.append(nums1[p_1])
                p_1 += 1
            else:
                res.append(nums2[p_2])
                p_2 += 1

            if p_1 == len(nums1):
                p_1 = -1

            if p_2 == len(nums2):
                p_2 = -1

    l = len(res)
    print(res)

    m = math.floor(l / 2)
    if l % 2 == 0:
        return (res[m - 1] + res[m]) / 2
    else:
        return res[m]


print(find_median_sorted_arrays(nums1=[1, 2, 5], nums2=[3, 4]))
