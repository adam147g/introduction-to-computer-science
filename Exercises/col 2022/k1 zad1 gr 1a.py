# „Obcięcie” liczby naturalnej polega na usunięciu z niej M początkowych i N końcowych cyfr, gdzie
# M, N ⩾ 0. Proszę napisać funkcję, która dla danej liczby naturalnej K zwraca największą liczbę
# pierwszą o różnych cyfrach jaką można uzyskać z obcięcia liczby K albo 0, gdy taka liczba nie
# istnieje. Na przykład dla liczby 1202742516 spośród obciętych liczb pierwszych: 2, 5, 7, 251, 2027
# liczbą spełniającą warunek jest liczba 251.

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** (1 / 2)) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_diff(n):
    t = [0] * 10
    while n > 0:
        t[n % 10] += 1
        if t[n % 10] > 1:
            return False
        n //= 10
    return True


def zad(x):
    max_ = 0
    len = 0
    y = x
    while y > 0:
        len += 1
        y //= 10
    for M in range(len):
        y = x % (10 ** (len - M))
        for N in range(len - M):
            if is_prime(y) and is_diff(y):
                max_ = max(max_, y)
            y //= 10
    return max_


print(zad(1202742516))
