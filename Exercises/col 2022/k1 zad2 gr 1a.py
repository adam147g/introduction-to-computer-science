# Dwie liczby naturalne są 4-zgodne, jeżeli po zapisaniu ich w systemie o podstawie 4, zbiory cyfr
# występujące w liczbie są identyczne. Na przykład:
# 1310 = 314 i 2310 = 1134
# 1810 = 1024 i 3310 = 2014
# 10710 = 12234 i 5710 = 3214.
# Dana jest tablica T[N] zawierająca N liczb naturalnych. Proszę napisać funkcję, która zwraca
# długość najdłuższego podciągu (niekoniecznie spójnego) złożonego z liczb 4-zgodnych.

def number_base_converter(number, base=4):
    if number == 0:
        return "0"
    a = ""
    hex = "0123"
    while number > 0:
        a = hex[number % base] + a
        number = number // base
    return a


def howmuch(x):
    x = int(x)
    t = [0] * 10
    while x > 0:
        t[x % 10] += 1
        x //= 10
    count = 0
    for i in range(10):
        if t[i] != 0:
            count += 1
    return count


def zad(T):
    biggest = 0
    t = []
    count = [0, 0]
    for i in T:
        a = howmuch(number_base_converter(i))
        t.append(a)
        biggest = max(biggest, a)
    for i in range(biggest):
        curr = 0
        for j in range(len(T)):
            if t[j] == i:
                curr += 1
        if curr > count[0]:
            count[0] = curr
            count[1] = i
    return count[0]


T = [1310, 314, 2310, 1134, 1810, 1024, 3310, 2014, 10710, 12234, 5710, 3214]
print(zad(T))
