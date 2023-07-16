"""
Proszę zmodyfikować poprzedni program aby wypisywał znalezione n-ki.
"enki" - wypisywanie n elementów tablicy, których iloczyn daje w wyniku product
"""


def print_ns(T, product, n, idx=0, ns=[]):
    if product == 1 and n == 0:
        for i in range(len(ns)):
            print(ns[i], end=" ")
        print()
        return 1
    if n == 0:
        return 0
    count = 0
    if n > 0:
        for i in range(idx, len(T)):
            if product % T[i] == 0:
                new_ns = ns[:]
                new_ns.append(T[i])
                count += print_ns(T, product // T[i], n - 1, i + 1, new_ns)
    return count


T = [4, 6, 1, 7, 8, 3, 8, 9, 4, 21, 6, 12, 9, 6, 2]
print(print_ns(T, 16, 3))
