"""
Tablica t[N] jest wypełniona liczbami naturalnymi. Skok z pola i-tego można wykonać na pola
o indeksach i+k, gdzie k jest czynnikiem pierwszym liczby t[i] (mniejszym od niej samej). Napisz
funkcję, która sprawdza, czy da się przejść z pola 0 do N-1 – jeśli się da, zwraca ilość skoków,
jeśli się nie da, zwraca -1.
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


def count_jumps(T, total_jumps, idx=0, step_counter=0):
    if idx == len(T) - 1:
        total_jumps[0] = step_counter
        return
    factors = prime_factors(T[idx])
    for i in range(len(factors)):
        if factors[i] + idx < len(T) and factors[i] < T[factors[i] + idx]:
            count_jumps(T, total_jumps, factors[i] + idx, step_counter + 1)


def is_move_possible(T):
    total_jumps = [-1]
    count_jumps(T, total_jumps)
    return total_jumps[0]


T = [20, 12, 13, 4, 16, 18, 20, 16, 9, 9]
print(is_move_possible(T))