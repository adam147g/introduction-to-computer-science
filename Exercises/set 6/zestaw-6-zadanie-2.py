# zadanie 2
'''
”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.
'''

from math import sqrt


def waga(n):
    w = 0
    i = 2
    while n > 1 and i <= sqrt(n):  # lub i**2<=n lub i<=n*0.5
        b = False
        while n % i == 0:
            b = True
            n //= i
        if b:  # if b==True
            w += 1
        i += 1

    if n > 1:
        w += 1

    return w


def podzadanie(t):
    def zadanie(wagi, s1=0, s2=0, s3=0, i=0):       # s1,s2,s3 - 3 zbiory, i - licznik
        if i == len(t):                             # jeśli przejdziemy do końca tablicy
            if s1 == s2 and s2 == s3:               # sprawdź czy zbiory są równe
                return True
            else:
                return False

        return zadanie(wagi, s1 + wagi[i], s2, s3, i + 1) or \
               zadanie(wagi, s1, s2 + wagi[i], s3, i + 1) or \
               zadanie(wagi, s1, s2, s3 + wagi[i], i + 1)  # dodawanie elementów do jakiejś tablicy

    suma = 0
    n = len(t)
    wagi = [0] * n
    for i in range(n):
        wagi[i] = waga(t[i])
        suma += wagi[i]
    # wpisywanie do tablicy 'wagi' wag (z funkcji) z tablicy t

    print(wagi)
    if suma % 3 != 0:
        return False
    return zadanie(wagi)


t1 = [1, 2, 6, 30, 64]
t2 = [1, 2, 6, 30, 64, 18]
print(podzadanie(t1))
print(podzadanie(t2))
