"""
Dana jest tablica T[N] zawierająca liczby naturalne. Po tablicy możemy przemieszczać się według
następującej zasady: z pola o indeksie i możemy przeskoczyć na pole o indeksie i+k jeżeli k jest
czynnikiem pierwszym liczby t[i] mniejszym od t[i]. Proszę napisać funkcję, która zwraca informację
czy jest możliwe przejście z pola o indeksie 0 na pole o indeksie N-1. Funkcja powinna zwrócić
liczbę wykonanych skoków lub wartość -1 jeżeli powyższe przejście nie jest możliwe.
"""
from math import sqrt


def prime_number(a):
    if a == 2 or a == 3:
        return True
    elif a < 2 or a % 2 == 0 or a % 3 == 0:
        return False
    else:
        i = 5
        while i <= sqrt(a):
            if a % i == 0:
                return False
            i += 2
            if a % i == 0:
                return False
            i += 4
        return True


def prime_factors(number):
    result = []
    if prime_number(number):
        result.append(number)
        return result
    actual = 2
    while number != 1:
        if prime_number(actual) and number % actual == 0:
            result.append(actual)
            while number % actual == 0:
                number //= actual
        actual += 1
    return result



def is_move_possible(T):
    total_jumps = -1


    def count_jumps(T,  idx=0, step_counter=0):
        nonlocal total_jumps
        if idx == len(T) - 1:
            total_jumps = step_counter
            return
        factors = prime_factors(T[idx])
        for i in range(len(factors)):
            if factors[i] + idx < len(T) and factors[i] < T[factors[i] + idx]:
                count_jumps(T,  factors[i] + idx, step_counter + 1)


    count_jumps(T)
    return total_jumps


T = [18, 2, 19, 16, 15, 4, 11, 8, 13, 14]
print(is_move_possible(T))