from random import randint
from math import sqrt


def prime_number(a):
    if a == 2 or a == 3:
        return True
    elif a < 2 or a % 2 == 0 or a % 3 == 0:
        return False
    else:
        i = 5
        while i <= sqrt(a):
            if a % i == 0:
                return False
            i += 2
            if a % i == 0:
                return False
            i += 4
        return True


def zad15(t):
    a, b = 1, 2
    while True:
        if a >= len(t):
            break
        else:
            if prime_number(t[a][0]):
                return False
            else:
                t[a] = (t[a][0], True)
                a = a + b
        if b >= len(t):
            break
        else:
            if prime_number(t[b][0]):
                return False
            else:
                t[b] = (t[b][0], True)
                b = a + b
    count = 0
    for i in range(len(t)):
        if not t[i][1]:
            if prime_number(t[i][0]):
                count += 1
        if count > 0:
            return True
    return False


# t = [(randint(1, 100),False) for _ in range(10)]
t = [randint(1, 1000) for _ in range(20)]
print(t)
for i in range(len(t)):
    t[i] = (t[i], False)

print(zad15(t))
print()
tab = [66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 2]
print(tab)
for i in range(len(tab)):
    tab[i] = (tab[i], False)
print(zad15(tab))