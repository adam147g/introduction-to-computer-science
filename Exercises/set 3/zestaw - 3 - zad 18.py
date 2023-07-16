def find_palindrom(t):
    len_t = len(t)
    max_len = 0
    for p in range(len_t):
        if t[p] % 2 == 1:
            for k in range(len_t - 1, p - 1, -1):
                cp = p
                ck = k
                while cp < ck:
                    if t[cp] != t[ck] or t[cp] % 2 == 0:
                        break
                    cp += 1
                    ck -= 1
                if not (cp < ck):
                    max_len = max(max_len, k - p + 1)
    return max_len

t1 = [1, 3, 3, 5, 2, 4, 4, 4, 1, 5, 1, 1, 5, 1, 4, 2, 6]
print(find_palindrom(t1))