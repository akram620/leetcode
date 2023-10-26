def is_almost_polindrome(word):
    i = 0
    j = len(word) - 1
    c = 0
    while i < j:
        if word[i] != word[j]:
            if c == 0:
                c += 1
            else:
                return False
        i += 1
        j -= 1
    return True


print(is_almost_polindrome('abccba'))
