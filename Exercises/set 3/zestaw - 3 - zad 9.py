"""
#MOJE ROZWIĄZANIE
from random import randint
def increasing_subsequence_check():
    t = list()
    x = list()
    N = 1000
    maximum = 0
    for i in range(N):
        x = randint(1, N)
        if x not in t:
            t.append(x)
        else:
            i -= 1
    t.sort()
    lengthn = len(t)
    x = [1]*lengthn
    for i in range(1, lengthn):
        for j in range(0, i):
            if t[i] > t[j] and x[i] < x[j] + 1:
                x[i] = x[j] + 1
        maximum = max(maximum, x[i])
    return maximum
print(increasing_subsequence_check())
"""
# ROZWIĄZANIE NA ĆWICZENIACH
from random import randint

def func(t):
    t_len = len(t)
    max_len = 1
    current = 1
    for i in range(1, t_len):
        if t[i] > t[i-1]:
            current += 1
        else:
            if current > max_len:
                max_len = current
            current = 1
    if current > max_len:
        max_len = current
    return max_len

tab = [randint(0, 9) for _ in range(10)]
print(tab)
print(func(tab))
