"""
Dana jest tablica T[N][N] wypełniona wartościami 0, 1. Każdy wiersz tablicy traktujemy jako liczbę zapisaną
w systemie dwójkowym o długości N bitów. Stała N jest rzędu 1000. Proszę zaimplementować funkcję
distance(T), która dla takiej tablicy wyznaczy dwa wiersze, dla których różnica zawartych w wierszach
liczb jest największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić odległość pomiędzy
znalezionymi wierszami. Można założyć, że żadne dwa wiersze nie zawierają identycznego ciągu cyfr.
"""


# zad2 Adam Górka
def cmp(T, a, b):
    n = len(T[a])
    i = 0
    while T[a][i] == T[b][i] and i < n - 1:
        i += 1
    return T[a][i] > T[b][i]


def distance(T):
    n = len(T)
    i_min = i_max = 0
    for i in range(n):
        if cmp(T, i, i_max):
            i_max = i
        if cmp(T, i_min, i):
            i_min = i
    return abs(i_max - i_min)


T = [[0, 0, 0, 0, 1, 1, 0, 1, 0],
     [0, 1, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 0, 1, 1],
     [0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0]]
print(distance(T))
