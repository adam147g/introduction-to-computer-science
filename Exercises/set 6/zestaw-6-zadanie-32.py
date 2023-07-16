"""
Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpowiada na
pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory
o jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy
przekazać wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool.
"""


def equal_sum_of_elements(T, k, summary=0, idx=0, count1=0, count2=0):
    if summary == 0 and count1 + count2 == k:
        return True
    elif idx == len(T):
        return False
    return (equal_sum_of_elements(T, k, summary + T[idx], idx + 1, count1 + 1, count2) or
            equal_sum_of_elements(T, k, summary - T[idx], idx + 1, count1, count2 + 1) or
            equal_sum_of_elements(T, k, summary, idx + 1, count1, count2))


T = [3, 6, 5, 23, 14, 23, 1, 19, 2, 7, 8, 15]
k = 11
print(equal_sum_of_elements(T, k, 0))