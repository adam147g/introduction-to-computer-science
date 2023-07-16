'''from random import randint
def find_the_longest_conseq_subseq():
    t = list()
    N = 1000
    i = 0
    summary = 0
    count = 0
    ans = 0
    for _ in range(1, N):
        x = randint(1, N)
        if x not in t:
            t.append(x)
        else:
            N -= 1
    t.sort()
    for element in t:
        summary += 1
    for i in range(summary):
        if i > 0 and t[i] == t[i-1] + 1:
            count += 1
        else:
            count = 1
        ans = max(ans, count)
    return ans

print(find_the_longest_conseq_subseq())'''


def zad11(tab):
    l_tab = len(tab)
    licz = 2
    licz_max = 2
    for i in range(l_tab - 2):
        if tab[i] != 0:
            q = tab[i + 1] / tab[i]
            if tab[i + 1] != 0 and (tab[i + 2] / tab[i + 1]) == q:
                licz += 1
            else:
                if licz > licz_max:
                    licz_max = licz
                    licz = 2

    return licz_max


tab = [0, -3, -6, 3, -1.5, 0.75, 9, -12, 0, 9, 5]
print(zad11(tab))
