def average(T, l):
    if l > 1:
        l_l, sr_l = average(T[:l//2], l//2)
        l_r, sr_r = average(T[l//2:], l-l//2)
        return l, (l_l*sr_l + l_r*sr_r) / l
    return 1, T[0]

T = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
res = average(T, len(T))
if res == (len(T),sum(T)/len(T)):
    print("Bravo",res)
