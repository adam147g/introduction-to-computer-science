"""
Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można wybrać
z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane elementy
nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
wartość sumy, funkcja powinna zwrócić wartość typu bool.
"""


def check(T, summary, rows, cols, current_sum=0, r=0, c=0):
    if current_sum == summary:
        return True
    if current_sum > summary:
        return False
    if c >= len(T):
        r += 1
        c = 0
    if r >= len(T):
        return False
    if rows[r] is False and cols[c] is False:
        rows[r] = cols[c] = True
        if check(T, summary, rows, cols, current_sum + T[r][c], r, c + 1):
            return True
        rows[r] = cols[c] = False
    if check(T, summary, rows, cols, current_sum, r, c + 1):
        return True
    return False


def subset_with_a_given_sum(T, summary):
    rows = [False] * len(T)
    cols = [False] * len(T)
    return check(T, summary, rows, cols)


T = [[1, 8, 14, 9],
     [2, 5, 11, 3],
     [12, 2, 6, 11],
     [13, 1, 8, 21]]
print(subset_with_a_given_sum(T, 18))