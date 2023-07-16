"""
Dana jest tablica T[N][N][N]. Proszę napisać funkcję, do której przekazujemy tablicę wypełnioną
liczbami większymi od zera. Funkcja powinna zwracać wartość True, jeżeli na wszystkich poziomach
tablicy liczba elementów sąsiadujących (w obrębia poziomu) z co najmniej 6 liczbami złożonymi jest
jednakowa albo wartość False w przeciwnym przypadku.
"""
from random import randint


def location_check(array):
    array_len = len(array)
    array_count = 0
    for i in range(array_len):
        row_count = 0
        for j in range(array_len):
            for k in range(array_len):
                cp = array[i][j][k]
                count = 0
                while cp > 0:
                    cp //= 10
                    count += 1
                if count > 1:
                    row_count += 1
                else:
                    row_count = 0
                    continue
            if row_count >= 6:
                array_count += 1
                break
        if row_count < 6:
            return False
    if array_count == array_len:
        return True
    return False


N = 5
array = [[[randint(1, 50) for _ in range(N)] for _ in range(N)] for _ in range(N)]
print(location_check(array))