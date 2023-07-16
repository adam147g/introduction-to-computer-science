"""
Używając funkcji z poprzedniego zadania proszę napisać funkcję rozwiązującą równanie kwadratowe
o współczynnikach zespolonych.
"""
from cmath import sqrt


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def power(a, n):
    z = a ** n
    return z


def complex_number_input(statement):
    complex_number = complex(input(statement))
    return complex_number


# y = a*x^2 + b*x + c
# enter complex number by typing x+yj e.g. 4+6j
a = complex_number_input("a = ")
b = complex_number_input("b = ")
c = complex_number_input("c = ")

discriminant = subtraction(power(b, 2), 4 * multiplication(a, c))
x1 = division(addition(-b, sqrt(discriminant)), 2)
x2 = division(subtraction(-b, sqrt(discriminant)), 2)

if discriminant == 0:
    print(x1)
else:
    print(x1)
    print(x2)