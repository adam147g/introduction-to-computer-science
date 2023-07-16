"""
Dana jest N-elementowa tablica t zawierająca liczby naturalne. W tablicy możemy przeskoczyć
z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby t[k].
Napisać funkcję sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.
"""
from random import randint


def crossing_check(N):
    T = [randint(1, 30) for _ in range(N)]
    print(T)
    visited = [False] * len(T)
    visited[0] = True
    for i in range(len(T)):
        if visited[i]:
            divisor = 2
            while T[i] > 1:
                while T[i] % divisor == 0:
                    if i + divisor < len(T):
                        visited[i + divisor] = True
                    T[i] //= divisor
                divisor += 1
    return visited[-1]


print(crossing_check(10))


# MOJE

def zad8(t, idx=0):
    if t[idx] < 2:
        return False
    i = 2
    copy = t[idx]
    while i <= copy:
        flag = False
        while copy % i == 0:
            copy //= i
            flag = True
        if flag:
            if idx + i == len(t) - 1:
                return True
            elif idx + i >= len(t):
                return False
            else:
                if zad8(t, idx + i):
                    return True
        i += 1
    return False


t_1 = [randint(0, 30) for _ in range(10)]
t_2 = [15, 0, 0, 0, 0, 15, 0, 0, 0, 0, 15, 0, 0, 9]
t_3 = [6, 0, 0, 4, 9, 1]
t_4 = [6, 0, 1, 3, 9, 1]
TESTS = [t_1, t_2, t_3, t_4]
print()
for t in TESTS:
    print(t)
    print(zad8(t))
