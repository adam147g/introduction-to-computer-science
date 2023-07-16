"""from random import randint


def addition(array):
    array_len = len(array)
    sum_result = 0
    for i in range(array_len):
        sum_result += array[i][0]/array[i][1]
    return sum_result


def substraction(array):
    substraction_result = 0
    array_len = len(array)
    for i in range(array_len):
        substraction_result -= array[i][0]/array[i][1]
    return substraction_result


def multiplication(array):
    multiplication_result = 1
    array_len = len(array)
    for i in range(array_len):
        multiplication_result *= array[i][0]/array[i][1]
    return multiplication_result


def division(array):
    division_result = 1
    array_len = len(array)
    for i in range(array_len-1):
        division_result = (array[i][0]/array[i][1]) / division_result
    return division_result


def exponentiation(array):
    exponentiation_result = 1
    array_len = len(array)
    for i in range(array_len):
        exponentiation_result = (array[i][0]/array[i][1])\
            ** exponentiation_result


def shortening(array):
    array_len = len(array)
    for i in range(array_len):
        if array[i][0] >= array[i][1]:
            for a in range(array[i][0]):
                if array[i][0] % a == 0 and array[i][1] % a == 0:
                    array[i][0] = array[i][0] / a
                    array[i][1] = array[i][1] / a
            result1 = array[i][0]/array[i][1]
            return result1
        else:
            for b in range(array[i][1]):
                if array[i][0] % b == 0 and array[i][1] % b == 0:
                    array[i][0] = array[i][0] / b
                    array[i][1] = array[i][1] / b
            result2 = array[i][0]/array[i][1]
            return result2


def print_element(array):
    array_len = len(array)
    for a in range(array_len):
        print(a)


def enter_element():
    numerator = int(input("Podaj licznik: "))
    denominator = int(input("Podaj mianownik: "))
    if denominator == 0:
        return "Mianownik nie może być ronwy 0!"
    fraction = numerator/denominator
    return fraction


n = int(input("Podaj liczbę pierwwiastków: "))
array = [(randint(-100, 100), randint(1, 100)) for _ in range(n)]"""


def dodawanie(a, b):
    return (a[0] * b[1] + b[0] * a[1], a[1] * b[1])


def odejmowanie(a, b):
    return (a[0] * b[1] - b[0] * a[1], a[1] * b[1])


def mnozenie(a, b):
    return (a[0] * b[0], a[1] * b[1])


def dzielenie(a, b):
    if b[0] == 0:
        return None
    return (a[0] * b[1], a[1] * b[0])


def potegowanie(a, b):
    if a == 0 and b == 0:
        return None
    return ((a[0] / a[1]) ** (b[0] / b[1]))


def skracanie(a):
    def NWD(x, y):
        x, y = abs(a), abs(b)
        while y != 0:
            y, x = x % y, y
            return x

    d = NWD(a[0], a[1])
    return a[0] // d, a[1] // d

