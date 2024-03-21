def majority_element(nums):
    count = 0
    num = nums[0]
    for i in nums:
        if count == 0:
            num = i
            count += 1
            continue

        if num == i:
            count += 1
        else:
            count -= 1
        print(num)

    return num


print(majority_element([6, 5, 5]))
