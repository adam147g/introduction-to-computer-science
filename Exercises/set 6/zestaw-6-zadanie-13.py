# zadanie 13
"""
Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę
składników. Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.
"""

def podzial_liczby(n, k=1, l=[]):
    if n == 0:
        print(l)
    else:
        for i in range(k, n + 1):
            podzial_liczby(n - i, i, l + [i])


podzial_liczby(5)
