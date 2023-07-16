"""
Dana jest tablica T zawierająca liczby wymierne reprezentowane w postaci ułamków. Ułamki reprezentowane
są w postaci krotek składających się z licznika i mianownika. Proszę napisać funkcję longest(T), zwracającą
długość najdłuższego spójnego podciągu, którego elementy stanowią ciąg geometryczny. W przypadku gdy
w tablicy nie ma ciągu dłuższego niż 2 elementy, funkcja powinna zwrócić wartość 0.
Komentarz: Można założyć, że tablica wejściowa liczy więcej niż 2 elementy.
Przykłady:
print(longest( [(0,2),(1,2),(2,2),(4,2),(4,1),(5,1)] ) # wypisze 4
print(longest( [(1,2),(-1,2),(1,2),(1,2),(1,3),(1,2)] ) # wypisze 3
print(longest( [(3,18),(-1,6),(7,42),(-1,6),(5,30),(-1,6)] ) # wypisze 6
print(longest( [(1,2),(2,3),(3,4),(4,5),(5,6)] ) # wypisze 0
"""


def longest(T):
    max_len = 0
    n = len(T)
    i = 0
    while i < n - 1:
        j = i + 1
        curr_len = 2
        if (T[j - 1][0] / T[j - 1][1]) != 0:
            q = (T[j][0] / T[j][1]) / (T[j - 1][0] / T[j - 1][1])
            while j < n - 1:
                if (T[j][0] / T[j][1]) != 0 and (T[j + 1][0] / T[j + 1][1]) / (T[j][0] / T[j][1]) == q:
                    curr_len += 1
                    j += 1
                else:
                    break
        if curr_len != 2 and curr_len > max_len:
            max_len = curr_len
        i += 1

    return max_len


print(longest([(0, 2), (1, 2), (2, 2), (4, 2), (4, 1), (5, 1)]))  # wypisze 4
print(longest([(1, 2), (-1, 2), (1, 2), (1, 2), (1, 3), (1, 2)]))  # wypisze 3
print(longest([(3, 18), (-1, 6), (7, 42), (-1, 6), (5, 30), (-1, 6)]))  # wypisze 6
print(longest([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]))  # wypisze 0
