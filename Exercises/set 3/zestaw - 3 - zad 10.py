'''def find_the_longest_arithmetic_progression(t):
    max_len = 0
    len_t = len(t)
    for p in range(len_t):
        for k in range(1, len_t-p):
            result = 1
            r = t[p+k] - t[p]
            cp = p
            ck = k
            while True:
                try:
                    if t[cp+ck] != t[cp] + r:
                        break
                    cp = cp + ck
                    result += 1
                except IndexError:
                    break
            if result > max_len:
                max_len = result
    return max_len

array = [1, 2, 3, 4, 5, 6, 7, 456, 2, 54, 48, 10, 11]
print(find_the_longest_arithmetic_progression(array))'''


# moje rozw
def zad10(tab):
    l_tab = len(tab)
    licz = 2
    licz_max = 2
    for i in range(l_tab - 2):
        r = tab[i + 1] - tab[i]
        if (tab[i + 2] - tab[i + 1]) == r:
            licz += 1
        else:
            if licz > licz_max:
                licz_max = licz
                licz = 2
    return licz_max


tab = [2, 1, 0, -3, -6, -9, 3, -6, 9, -12, 9, 5]
print(zad10(tab))
