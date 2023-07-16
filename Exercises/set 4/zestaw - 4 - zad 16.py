"""
Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję która odpowiada
na pytanie, czy w tablicy każdy wiersz zawiera co najmniej jedną liczbą złożoną wyłącznie z cyfr
będących liczbami pierwszymi?
"""
from random import randint
from math import sqrt, log10


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


def complex_number(array):
    row_count = 0
    main_count = 0
    for i in range(len(array)):
        row_count += 1
        for j in range(len(array)):
            digits = int(log10(array[i][j]) + 1)
            number = str(array[i][j])
            count = 0
            for x in number:
                x_number = int(x)
                if prime_number(x_number):
                    count += 1
            if count == digits:
                main_count += 1
                break
    if row_count == main_count:
        return True
    return False


N = 3
array = [[randint(20, 30) for _ in range(N)] for _ in range(N)]
print(complex_number(array))