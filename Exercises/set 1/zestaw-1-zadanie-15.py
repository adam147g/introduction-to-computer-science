"""
Nieskończony iloczyn sqrt(0.5) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5)) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5 + 0.5 ∗
sqrt(0.5))) ∗ ... ma wartość 2/π. Napisz program korzystający z tej zależności i wyznaczający wartość π.
"""
from math import sqrt

a = sqrt(0.5)
x = sqrt(0.5 + 0.5 * a)
result = a * x
num = int(input("Enter range: "))

for i in range(num):
    x = sqrt(0.5 + 0.5 * x)
    result = result * x
pi = 2 / result
print(pi)