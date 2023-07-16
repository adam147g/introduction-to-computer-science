"""
Dwie liczby naturalne są zgodne jeżeli w zapisie dwójkowym zawierają tę samą liczbę jedynek,
np. 22 = 10110(2) i 14 = 1110(2). Dane są tablice T1[N1][N1] T2[N2][N2], gdzie N2>N1. Proszę
napisać funkcję, która sprawdza czy istnieje takie położenie tablicy T1 wewnątrz tablicy T2,
przy którym liczba zgodnych elementów jest większa od 33%. Do funkcji należy przekazać
tablicę T1 i T2. Obie oryginalne tablice powinny pozostać nie zmieniane.

"""


def convert_number_to_binary_and_count(number):
    count = 0
    while number > 0:
        count += number % 2
        number //= 2
    return count


def change_array(T):
    for i in range(len(T)):
        for j in range(len(T)):
            T[i][j] = convert_number_to_binary_and_count(T[i][j])
    return T


def check_arrays(T1, T2, idx1, idx2):
    if len(T2) > len(T1) + idx2:
        return 0
    count = 0
    for i in range(len(T1)):
        if len(T2[i]) > len(T1[i]) + idx1:
            return 0
        for j in range(len(T1[i])):
            if T1[i][j] == T2[i + idx2][j + idx1]:
                count += 1
    return count


def matching_numbers_in_array(T1, T2):
    changed_T1 = change_array(T1)
    changed_T2 = change_array(T2)
    for i in range(len(T2) - len(T1) + 1):
        for j in range(len(T2) - len(T1) + 1):
            if check_arrays(changed_T1, changed_T2, i, j) / (len(changed_T1) ** 2) > 1 / 3:
                return True
    return False


T1 = [[8, 7],
      [9, 3]]
T2 = [[11, 15, 6],
      [17, 4, 15],
      [3, 2, 5]]
print(matching_numbers_in_array(T1, T2))
