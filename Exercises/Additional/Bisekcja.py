from math import sin


def bisekcja_m_zerowe(f, x1, x2, eps):
    while abs(f((x1 + x2) / 2)) > eps:
        if f(x1) * f((x1 + x2) / 2) < 0:
            x2 = (x1 + x2) / 2
        else:
            x1 = (x1 + x2) / 2
    return round((x1 + x2) / 2, 10)


def func_1(x):
    return sin(x)

def func_2(x):
    return x ** 3 - 2 * x ** 2 + 4 * x - 1


print(bisekcja_m_zerowe(func_1, -1.5, 1, 0.000000000001))
print(bisekcja_m_zerowe(func_2, -10, 10, 0.001))
