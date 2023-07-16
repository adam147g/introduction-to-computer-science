"""
Rekurencyjne obliczanie wyznacznika z macierzy (treść oczywista).
"""
# import numpy as np


# RECURSION SOLUTION


def calculate_minor(minor, x, y):
    return [row[: y] + row[y + 1:] for row in (minor[:x] + minor[x + 1:])]


def determinant_of_matrix(array):
    if (len(array) == 2):
        determinant = array[0][0] * array[1][1] - array[0][1] * array[1][0]
        return determinant
    summary = 0
    for i in range(len(array)):
        algebraic_complement = (-1) ** i
        determinant_subset = determinant_of_matrix(calculate_minor(array, 0, i))
        summary += (algebraic_complement * array[0][i] * determinant_subset)
    return summary


N = 5
array = [[1, 3, 1, 4],
         [3, 9, 5, 15],
         [0, 2, 1, 1],
         [7, 3, 4, 2]]
print(determinant_of_matrix(array))

'''
# NUMPY SOLUTION


def numpy_determinant(N):
    np_array = np.array([[1, 3, 1, 4],
                         [3, 9, 5, 15],
                         [0, 2, 1, 1],
                         [7, 3, 4, 2]])
    determinant = np.linalg.det(np_array)
    return round(determinant)

N = 5
print(numpy_determinant(N))
'''