"""
Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. Proszę napisać funkcję, która wyszuka
spójny podciąg elementów leżący poziomo lub pionowo o największej sumie. Maksymalna długość
podciągu może wynosić 10 elementów. Do funkcji należy przekazać tablicę T, funkcja powinna zwrócić
sumę maksymalnego podciągu.
"""
from random import randint


def find__the_longest_summertree(array):
    array_len = len(array)
    row_result = 0
    column_result = 0
    max_row_result = 0
    max_column_result = 0
    for i in range(array_len):
        for j in range(array_len - i - 1):
            if array[i][j] < array[i + 1][j + 1]:
                row_result += 1
                if row_result > max_row_result:
                    if row_result <= 10:
                        max_row_result = row_result
            else:
                row_result = 0

    for a in range(array_len):
        for b in range(array_len - i - 1):
            if array[b][a] < array[b + 1][a + 1]:
                column_result += 1
                if column_result > max_column_result:
                    if column_result <= 10:
                        max_column_result = column_result
            else:
                column_result = 0

    if max_column_result >= max_row_result:
        return max_column_result
    elif max_row_result >= max_column_result:
        return max_row_result


N = 10
array = [[randint(-50, 50) for _ in range(N)] for _ in range(N)]
print(find__the_longest_summertree(array))