from typing import List


def spiral_order_yandex(matrix: List[List[int]]) -> List[int]:

    for i in matrix:
        print(i)

    result_numbers = []

    hor_top = 0
    hor_bot = len(matrix) - 1

    ver_left = 0
    ver_right = len(matrix[0]) - 1

    cur_hor = 0
    cur_ver = 0

    max_len = len(matrix) * len(matrix[0])

    direction = 'r'
    while True:
        result_numbers.append(int(matrix[cur_hor][cur_ver]))

        if len(result_numbers) == max_len:
            break

        if direction == 'r':
            if cur_ver < ver_right:
                cur_ver += 1
            else:
                direction = 'b'
                hor_top += 1

        if direction == 'b':
            if cur_hor < hor_bot:
                cur_hor += 1
            else:
                direction = 'l'
                ver_right -= 1

        if direction == 'l':
            if cur_ver > ver_left:
                cur_ver -= 1
            else:
                direction = 't'
                hor_bot -= 1

        if direction == 't':
            if cur_hor > hor_top:
                cur_hor -= 1
            else:
                direction = 'r'
                ver_left += 1
                cur_ver += 1

    return result_numbers


res = spiral_order_yandex([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(res)

# [1, 2, 3, 6, 9, 8, 7, 4, 5]
# [1, 2, 3, 6, 9, 8, 7, 4, 5]

