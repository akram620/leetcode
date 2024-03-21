from typing import List


def spiral_order_avito() -> List[int]:
    with open('matrix.txt', 'r') as f:
        lines = f.readlines()

        matrix_list = []
        result_numbers = []

        for i in range(len(lines)):
            print(lines[i])
            if i % 2 == 1:
                line = lines[i].replace(' ', '').split('|')[1:-1]
                matrix_list.append(line)

        hor_top = 0
        hor_bot = len(matrix_list) - 1

        ver_left = 0
        ver_right = len(matrix_list[0]) - 1

        cur_hor = 0
        cur_ver = 0

        max_len = len(matrix_list) * len(matrix_list[0])

        direction = 'b'
        while True:
            result_numbers.append(int(matrix_list[cur_hor][cur_ver]))

            if len(result_numbers) == max_len:
                break

            if direction == 'b':
                if cur_hor < hor_bot:
                    cur_hor += 1
                else:
                    direction = 'r'
                    ver_left += 1

            if direction == 'r':
                if cur_ver < ver_right:
                    cur_ver += 1
                else:
                    direction = 't'
                    hor_bot -= 1

            if direction == 't':
                if cur_hor > hor_top:
                    cur_hor -= 1
                else:
                    direction = 'l'
                    ver_right -= 1

            if direction == 'l':
                if cur_ver > ver_left:
                    cur_ver -= 1
                else:
                    direction = 'b'
                    hor_top -= 1
                    cur_hor += 1

        print(result_numbers)

        return result_numbers
