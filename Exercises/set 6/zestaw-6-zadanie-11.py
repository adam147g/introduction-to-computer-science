"""
Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym iloczynie.
"enki" - wypisywanie n elementów tablicy, których iloczyn daje w wyniku product
"""


def number_of_ns(T, product, n, idx=0):
    if product == 1 and n == 0:
        return 1
    if n == 0:
        return 0
    count = 0
    if n > 0:
        for i in range(idx, len(T)):
            if product % T[i] == 0:
                count += number_of_ns(T, product // T[i], n - 1, i + 1)
    return count


T = [4, 6, 1, 7, 8, 3, 8, 9, 4, 21, 6, 12, 9, 6, 2]
print(number_of_ns(T, 16, 3))
