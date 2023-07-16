"""
Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie M=N*N.
W każdym wierszu tablicy T1 znajdują się uporządkowane niemalejąco (w obrębie wiersza) liczby naturalne.
Proszę napisać funkcję przepisującą wszystkie liczby z tablicy T1 do T2, tak aby liczby w tablicy
T2 były uporządkowane niemalejąco.
"""
from random import randint


def non_decreasing_elements(array1, array2, M, N, indexes):
    for i in range(M):
        add = 0
        min_ = 100000000
        for row in range(N):
            if indexes[row] < N and array1[row][indexes[row]] <= min_:
                min_ = array1[row][indexes[row]]
                add = row
        array2[i] = min_
        indexes[add] += 1

    return array2


N = 4
M = N ** 2
array1 = [[randint(1, 20) for _ in range(N)] for _ in range(N)]
for i in range(len(array1)):
    array1[i].sort()
    print(array1[i])

array2 = [0 for i in range(M)]
indexes = [0 for i in range(N)]
print(non_decreasing_elements(array1, array2, M, N, indexes))
