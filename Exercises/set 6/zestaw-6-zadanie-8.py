"""
Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach.
"""
from random import randint


def is_both_mass(array, n, p=0):
    if n == 0:
        return True
    elif p == len(array):
        return False
    return (is_both_mass(array, n - array[p], p + 1)
         or is_both_mass(array, n, p + 1)
         or is_both_mass(array, n + array[p], p + 1))


N = 4
number = 20
array = [randint(1, 10) for _ in range(N)]
print(array)
print(is_both_mass(array, number))
