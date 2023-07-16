"""
Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na „szachowanych”
przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić
położenie wież. Uwaga: zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem
pola na którym stoi.
"""


def column_summary(array, row, col):
    result = 0
    for i in range(len(array)):
        result += array[i][col]
    result -= array[row][col]
    return result


def row_summary(array, row, col):
    result = 0
    for i in range(len(array)):
        result += array[row][i]
    result -= array[row][col]
    return result


def two_rooks(array):
    max_result = 0
    tower_1 = tower_2 = 0
    for i in range(len(array)):
        for j in range(len(array)):
            for k in range(i, len(array)):
                for m in range(len(array)):
                    if i != k and j != m:
                        result = column_summary(array, i, j) + column_summary(array, k, m) \
                                 + row_summary(array, i, j) + row_summary(array, k, m)
                        result -= array[i][m]
                        result -= array[k][j]
                        if result > max_result:
                            tower_1 = (i, j)
                            tower_2 = (k, m)
                            max_result = result
    return tower_1[0], tower_1[1], tower_2[0], tower_2[1]


array = [[1, 1, 2, 3],
         [-1, 3, -1, 4],
         [4, 1, 5, 4],
         [5, 0, 3, 6]]
print(two_rooks(array))