"""
Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną i zwraca sumę iloczynów
elementów wszystkich niepustych podzbiorów zbioru podzielników pierwszych tej liczby. Można założyć,
że liczba podzielników pierwszych nie przekracza 20, zatem w pierwszym etapie funkcja powinna wpisać
podzielniki do tablicy pomocniczej.
Przykład: 60 → [2, 3, 5] → 2 + 3 + 5 + 2 ∗ 3 + 2 ∗ 5 + 3 ∗ 5 + 2 ∗ 3 ∗ 5 = 71.
"""


def number_aliquot(n):
    array = []
    i, j = 2, 0
    while n > 1:
        if n % i == 0:
            array.append(i)
            j += 1
            while n % i == 0:
                n //= i
        i += 1
    return multiple_aliquot(array)


def multiple_aliquot(array, list_of_numbers=[], number=1, i=0):
    if i < len(array):
        return (multiple_aliquot(array, list_of_numbers, number * array[i], i + 1) or
                multiple_aliquot(array, list_of_numbers, number, i + 1))
    list_of_numbers.append(number)
    if list_of_numbers[-1] == 1:
        return sum(list_of_numbers[:-1])


print(number_aliquot(60))