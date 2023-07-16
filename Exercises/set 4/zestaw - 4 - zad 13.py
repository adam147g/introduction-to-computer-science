"""
Liczby naturalne a, b są komplementarne jeżeli ich suma jest liczbą pierwszą. Dana jest tablica
T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która zeruje elementy nie
posiadające liczby komplementarnej.
"""

# IMO żle jest

from random import randint
from math import sqrt
from copy import deepcopy


def prime_number(a):
    if a == 2 or a == 3:
        return True
    elif a < 2 or a % 2 == 0 or a % 3 == 0:
        return False
    else:
        i = 5
        while i <= sqrt(a):
            if a % i == 0:
                return False
            i += 2
            if a % i == 0:
                return False
            i += 4
        return True


def complementary_numbers(array, copy_array):
    array_len = len(array)
    for i in range(array_len):
        for j in range(array_len - 1):
            summary = array[i][j] + array[i][j + 1]
            if not prime_number(summary):
                copy_array[i][j] = 0
                copy_array[i][j + 1] = 0
            else:
                copy_array[i][j] = array[i][j]
                copy_array[i][j + 1] = array[i][j + 1]
    return copy_array


N = 5
array = [[randint(1, 20) for _ in range(N)] for _ in range(N)]
copy_array = deepcopy(array)
print(array)
print(complementary_numbers(array, copy_array))