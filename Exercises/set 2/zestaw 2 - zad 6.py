"""
Napisać program wczytujący liczbę naturalną z klawiatury i rozkładający ją na iloczyn 2 liczb
o najmniejszej różnicy. Np. 30 = 5 ∗ 6, 120 = 10 ∗ 12.
"""
from math import sqrt

number = int(input("Enter a number: "))
i = int(sqrt(number))
while number % i != 0:
    i += 1

print(number, "=", round(i), "*", round(number / i))
