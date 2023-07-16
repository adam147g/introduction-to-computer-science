# Liczbę nazywamy iloczynowo-pierwszą jeżeli iloczyn jej cyfr w systemie o podstawie b jest liczbą
# pierwszą. Na przykład:
# 13 jest liczbą iloczynowo-pierwszą w systemie dziesiętnym, bo 1 · 3 = 3.
# 16 jest liczbą iloczynowo-pierwszą w systemie trójkowym, bo 16(10) = 121(3), 1 · 2 · 1 = 2.
# W liczbie naturalnej możemy dokonywać rotacji jej cyfr, np. 1428, 4281, 2814, 8142 albo 209, 092,
# 920.
# Proszę napisać funkcję, która dla danej liczby naturalnej N, zwróci najmniejszą podstawę systemu (z
# zakresu 2-16) w którym przynajmniej jedna z rotowanych liczb jest iloczynowo-pierwsza albo wartość
# None, gdy taka podstawa nie istnieje.

def number_base_converter(number, base):
    if number == 0:
        return "0"
    a = ""
    hex = "0123456789ABCDEF"
    while number > 0:
        a = hex[number % base] + a
        number = number // base
    return a


def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** (1 / 2)) + 1, 2):
        if n % i == 0:
            return False
    return True


def rotate(x, k):
    y = ''
    for i in range(len(x)):
        y = y + x[(i + k) % len(x)]
    return y


def zad(x):
    for i in range(2, 17):
        x = str(x)
        for j in range(len(x)):
            y = number_base_converter(int(x), i)
            ilocz = 1
            for k in range(len(y)):
                if y[k] not in 'ABCDEF':
                    ilocz *= int(y[k])
            if is_prime(ilocz):
                print("{0}({1}) = {2}".format(x,i,y))
                return i
            x = rotate(x, j + 1)
    return None


print(zad(13))
print(zad(1428))