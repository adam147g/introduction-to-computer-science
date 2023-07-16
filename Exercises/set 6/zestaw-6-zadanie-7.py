"""
Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie
określonej masy. Odważniki można umieszczać tylko na jednej szalce.
"""
from random import randint


def is_mass(array, n, p):
    if n == 0:
        return True
    if p == len(array):
        return False
    return is_mass(array, n - array[p], p + 1) or is_mass(array, n, p + 1)


N = 5
array = [randint(1, 10) for _ in range(N)]
print(array)

for i in range(1, 50):
    print(i, is_mass(array, i, 0))