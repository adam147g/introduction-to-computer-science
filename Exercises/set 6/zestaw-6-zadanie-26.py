"""
Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A cyfr 1 oraz B cyfr 0,
gdzie A, B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca ilość wszystkich
możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym (najstarszy bit) jest
równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
10010(2), 10100(2), 11000(2).
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


def count_built_numbers(A, B, T, idx):
    count = 0
    if A == 0 and B == 0:
        temporary = 0
        for i in range(len(T)):
            temporary = temporary * 2 + T[i]
        if not prime_number(temporary):
            count += 1
    if A != 0:
        T[idx] = 1
        count += count_built_numbers(A - 1, B, T, idx + 1)
        T[idx] = 0
    if B != 0:
        count += count_built_numbers(A, B - 1, T, idx + 1)
    return count


def build_a_number(A, B):
    max_number = A + B
    T = [0] * max_number
    T[0] = 1
    return count_built_numbers(A - 1, B, T, 1)


print(build_a_number(2, 3))