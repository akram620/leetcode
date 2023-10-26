# 33/46 testcases passed (Memory Limit Exceeded)
# can not passed: 
# s = "y959q969u3hb22odq595"
# k = 222280369
def decode_at_index_1(s, k):
    pointer = 0

    res = []
    cur_len = 0

    # a2b3c4d5e6f7g8h9
    while cur_len < k:
        if s[pointer].isdigit():
            qnt = int(s[pointer]) - 1
            new_s = "".join(res)

            res.append(new_s * qnt)
            cur_len += len(new_s) * qnt

        else:
            res.append(s[pointer])
            cur_len += 1

        pointer += 1

    return "".join(res)[k - 1]


# 36/46 testcases passed (Memory Limit Exceeded)
# can not passed: 
# s = "cpmxv8ewnfk3xxcilcmm68d2ygc88daomywc3imncfjgtwj8nrxjtwhiem5nzqnicxzo248g52y72v3yujqpvqcssrofd99lkovg"
# k = 480551547

def decode_at_index_2(s, k):
    pointer = 0

    cur_len = 0

    last_str = ""
    last_len = 1

    # leet2code3
    while cur_len < k:
        if s[pointer].isdigit():
            qnt = int(s[pointer])
            last_len = qnt
            last_str = last_str * last_len
            cur_len = len(last_str)
        else:
            last_str += s[pointer]
            cur_len += 1

        pointer += 1

    return last_str[k - 1]


# 46/46 Accepted

def decode_at_index_3(s, k):
    l = len(s)
    if not s[l - 1].isdigit():
        s += '1'
        l += 1

    res_str = []
    res_qnt = []
    res_len = []

    start = 0

    cur_len = 0

    last_latter = ''
    two_digit = False

    # leet2code
    for pointer in range(l):
        if s[pointer].isdigit():
            # str
            new_str = s[start:pointer]

            if two_digit:
                res_str.append(last_latter)
            else:
                res_str.append(new_str)
            two_digit = True
            start = pointer + 1

            # qnt
            new_qnt = int(s[pointer])
            res_qnt.append(new_qnt)

            # len
            new_len = len(new_str)
            if cur_len == 0:
                res_len.append(new_len)
            else:
                res_len.append(cur_len + new_len)

            # cur_len
            cur_len = (cur_len + new_len) * new_qnt
        else:
            cur_len + 1
            last_latter = s[pointer]
            two_digit = False

        pointer += 1

    print(res_str)
    print(res_qnt)
    print(res_len)

    for i in range(len(res_str) - 1, 0, -1):
        v_len = res_len[i]
        prev_len = res_len[i - 1] * res_qnt[i - 1]

        mod = k % v_len

        if mod == 0:
            return res_str[i][-1]
        elif mod > prev_len:
            return res_str[i][mod - prev_len - 1]
        else:
            k = mod
            continue

    print('k:', k)
    total_len = res_len[0] * res_qnt[0]
    mod = k % total_len
    return (res_str[0] * res_qnt[0])[mod - 1]


s = decode_at_index_3(s="a23", k=6)
print(s)
