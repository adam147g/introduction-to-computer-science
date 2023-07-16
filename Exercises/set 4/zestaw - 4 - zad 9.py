"""
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która poszukuje
w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól
narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić
informacje czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu.
"""
from random import randint


def find_square(array, k):
    array_len = len(array)
    array_len_2 = array_len // 2
    for i in range(array_len // 2):
        if array_len % 2 == 1 and array_len > 1:
            for j in range(array_len // 2):
                if (array[0 + j][0 + j] * array[0 + j][-1 - j] * array[-1 - j][0 + j] * array[-1 - j][-1 - j]) == k:
                    return True, array[array_len_2][array_len_2]
    return False


N = 5
k = 0
array = [[randint(0, 10) for _ in range(N)] for _ in range(N)]
for i in range(N):
    print(array[i])
print(find_square(array, k))