"""
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję która zwraca
wiersz i kolumnę dowolnego elementu, dla którego suma otaczających go elementów jest największa.
"""
from random import randint


def max_sum_of_surrounding_elements(array):
    array_len = len(array)
    results = []
    positions = []

    # 1st square in 0 row with 2 blocks around
    result1 = array[0][1] + array[1][0]
    results += [result1]
    positions += [(0, 0)]

    # last square in 0 row with 2 blocks around
    result2 = array[0][array_len - 2] + array[1][-1]
    results += [result2]
    positions += [(0, array_len - 1)]

    # 1st square in last row with 2 blocks around
    result3 = array[-2][0] + array[-1][1]
    results += [result3]
    positions += [(array_len - 1, 0)]

    # last square in last row with 2 blocks around
    result4 = array[-2][-1] + array[-1][-2]
    results += [result4]
    positions += [(array_len - 1, array_len - 1)]

    # squares in 1st row with 3 blocks around
    for z in range(1, array_len - 1):
        result = array[0][z - 1] + array[0][z + 1] + array[1][z]
        results += [result]
        positions += [(0, z)]

    # squares in last row with 3 blocks around
    for x in range(1, array_len - 1):
        result = 0
        result = array[-1][x - 1] + array[-1][x + 1] + array[-2][x]
        results += [result]
        positions += [(array_len - 1, x)]

    # squares in 1st column with 3 blocks around
    for c in range(1, array_len - 1):
        result = array[c - 1][0] + array[c + 1][0] + array[c][1]
        results += [result]
        positions += [(c, 0)]

    # squares in last column with 3 blocks around
    for v in range(1, array_len - 1):
        result = array[v - 1][-1] + array[v + 1][-1] + array[v][-2]
        results += [result]
        positions += [(v, array_len - 1)]

    # square with 4 blocks around
    for i in range(1, array_len - 1):
        for j in range(1, array_len - 1):
            ci = i
            cj = j
            result = array[ci][cj + 1] + array[ci][cj - 1] + array[ci + 1][cj] + array[ci - 1][cj]
            results += [result]
            positions += [(i, j)]

    max_index = results.index(max(results))
    return positions[max_index]


N = 8
array = [[randint(0, 10) for _ in range(N)] for _ in range(N)]
print(max_sum_of_surrounding_elements(array))