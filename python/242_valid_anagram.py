def is_anagram(s, t):
    s_m = {}
    t_m = {}

    if len(s) != len(t):
        return False

    for i in s:
        if i not in s_m:
            s_m[i] = 0
        s_m[i] += 1

    for i in t:
        if i not in t_m:
            t_m[i] = 0
        t_m[i] += 1

    c = 0
    for i in s_m:
        if i not in t_m or s_m[i] != t_m[i]:
            return False
        else:
            c += 1
    if c == len(t_m):
        return True
    return False
