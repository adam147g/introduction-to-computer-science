"""
Dana jest tablica zawierająca liczby wymierne. Proszę napisać funkcję, która policzy występujące
w tablicy ciągi arytmetyczne (LA) i geometryczne (LG) o długości większej niż 2. Funkcja powinna
zwrócić wartość 1 gdy LA > LG, wartość -1 gdy LA < LG oraz 0 gdy LA = LG.
"""


def sequences_longer_than_two(T):
    LA = LG = 1
    r = T[1] - T[0]
    q = T[1] / T[0]
    actual_LA = actual_LG = 1
    for i in range(2, len(T)):
        if T[i] - T[i - 1] == r:
            actual_LA += 1
            LA = max(LA, actual_LA)
        else:
            r = T[i] - T[i - 1]
            actual_LA = 2
        if T[i] / T[i - 1] == q:
            actual_LG += 1
            LG = max(LG, actual_LG)
        else:
            q = T[i] / T[i - 1]
            actual_LG = 2
    if LA > LG:
        return 1
    elif LA < LG:
        return -1
    return 0


T = [23, 53, 12, 6, 23, 46, 1, 2, 4, 8]
print(sequences_longer_than_two(T))