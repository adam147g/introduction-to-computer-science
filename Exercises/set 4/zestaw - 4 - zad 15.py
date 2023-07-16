"""
Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję, która odpowiada
na pytanie, czy w tablicy istnieje wiersz, w którym każda liczba zawiera co najmniej jedną cyfrę
będącą liczbą pierwszą?
"""
from random import randint
from math import sqrt


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


def prime_numbers_in_row(array):
    for i in range(len(array)):
        number_count = 0
        count = 0
        for j in range(N):
            number = str(array[i][j])
            number_count += 1
            for x in number:
                x_number = int(x)
                if prime_number(x_number):
                    count += 1
                    break
        if count == number_count:
            return True
    return False


N = 3
array = [[randint(2, 20) for _ in range(N)] for _ in range(N)]
print(prime_numbers_in_row(array))