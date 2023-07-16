"""
Dwie liczby naturalne są „przyjaciółkami" jeżeli zbiory cyfr z których zbudowane są liczby
są identyczne. Na przykład: 123 i 321, 211 i 122, 35 i 3553. Dana jest tablica T[N][N] wypełniona
liczbami naturalnymi. Proszę napisać funkcję, która dla tablicy T zwraca ile elementów tablicy
sąsiaduje wyłącznie z przyjaciółkami.
"""
from random import randint


def friend(array, my_row, my_col, new_row, new_col):
    numbers_me = [0] * 10
    numbers_new = [0] * 10
    copy_me = array[my_row][my_col]
    copy_new = array[new_row][new_col]
    if copy_me == 0:
        numbers_me[0] += 1
    while copy_me > 0:
        numbers_me[copy_me % 10] += 1
        copy_me //= 10
    if copy_new == 0:
        numbers_new[0] += 1
    while copy_new > 0:
        numbers_new[copy_new % 10] += 1
        copy_new //= 10
    for i in range(len(numbers_me)):
        if (numbers_me[i] > 0 and numbers_new[i] == 0) or (numbers_new[i] > 0 and numbers_me[i] == 0):
            return False
    return True


def friends_numbers(array):
    result = 0
    for i in range(len(array)):
        for j in range(len(array)):
            flag = True
            if i - 1 > -1 and not friend(array, i, j, i - 1, j):
                flag = False

            if j - 1 > -1 and not friend(array, i, j, i, j - 1) and flag:
                flag = False

            if i + 1 < len(array) and not friend(array, i, j, i + 1, j) and flag:
                flag = False

            if j + 1 < len(array) and not friend(array, i, j, i, j + 1) and flag:
                flag = False
            if flag:
                print(array[i][j],i,j)
                result += 1
    return result


N = 10
array = [[ 1,   6,  23],
         [23, 223, 332],
         [ 0,  32,  32]]
for i in range(len(array)):
    print(array[i])
print(friends_numbers(array))
print()
array=[[randint(0,3) for _ in range(N)]for __ in range(N)]
for i in range(N):
    print(array[i])
print(friends_numbers(array))
