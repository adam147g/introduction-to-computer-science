"""
Poprzednie zadanie. Program powinien wypisywać wybrane odważniki.
"""
from random import randint


def is_both_mass_weights(array, n, p=0, result=[]):
    if n == 0:
        print(result)
        return True
    elif p == len(array):
        return False
    return (is_both_mass_weights(array, n - array[p], p + 1, result + [array[p]])
         or is_both_mass_weights(array, n, p + 1, result)
         or is_both_mass_weights(array, n + array[p], p + 1, result + [-array[p]]))


N = 5
T = [randint(1, 30) for _ in range(N)]
print(T)
print(is_both_mass_weights(T, 20))