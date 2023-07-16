"""
Zmodyfikować wzór Newtona aby program z zadania 5 obliczał pierwiastek stopnia 3.
"""
number = int(input("Enter a number: "))
a, b = 1, number
epsilon = 0.000000001

while abs(b - a) > epsilon:
    a = b
    b = (1 / 3) * ((3 - 1) * a + number / (a ** (3 - 1)))
print(b)