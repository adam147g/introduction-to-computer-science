# Dana jest N-elementowa tablica T, zawierająca liczby. Proszę napisać funkcję, która zwróci indeks
# największej liczby, która jest iloczynem wszystkich liczb pierwszych leżących w tablicy na indeksach
# mniejszych od niej lub None, jeżeli taka liczba nie istnieje.


def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** (1 / 2)) + 1, 2):
        if n % i == 0:
            return False
    return True


def zad(T):
    primes = [False] * len(T)
    for i in range(len(T)):
        primes[i] = is_prime(T[i])
    ilocz = 1
    idx = -1
    for i in range(len(T)):
        if T[i] > 1 and ilocz == T[i]:
            idx = i
        if primes[i]:
            ilocz *= T[i]
    if idx > -1:
        return idx
    return None


T_1 = [5, 6, 4, 8, 10, 7, 35, 3, 105, 1000]
T_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(zad(T_1))
print(zad(T_2))
