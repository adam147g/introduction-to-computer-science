"""
Napisać funkcję która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, zwraca wartość
True w przypadku, gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0 oraz
wartość False w przeciwnym przypadku.
"""
from random import randint


def is_there_at_least_one_zero(array):
    result = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] == 0:
                result += 1
                break
    for a in range(len(array)):
        for b in range(len(array)):
            if array[b][a] == 0:
                result += 1
                break
    if result == 2 * len(array):
        return True
    return False


N = 4
# array = [[randint(0, 3) for _ in range(N)] for _ in range(N)]
array = [[0, 1, 1, 1], [2, 0, 1, 3], [3, 2, 0, 1], [3, 0, 0, 0]]
print(array)
print(is_there_at_least_one_zero(array))