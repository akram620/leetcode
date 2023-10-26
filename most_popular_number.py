def most_popular_number(nums):
    dic = {}
    max_num = nums[0]
    max_count = 1
    for i in nums:
        if i not in dic:
            dic[i] = 0
        dic[i] += 1

        c = dic[i]

        if c > max_count:
            max_count = c
            max_num = i

        if c == max_count:
            if i < max_num:
                max_num = i
                max_count = c

    print(max_num)
    print(max_count)


most_popular_number([1, 2, 3, 4, 1, 1, 2, 2, 2, 1, 0, 0, 0, 0, 0])
