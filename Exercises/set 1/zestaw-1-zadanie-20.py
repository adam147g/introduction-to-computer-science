"""
Dane są ciągi: A[n+1] = sqrt(A[n] ∗ B[n]) oraz B[n+1] = (A[n] + B[n])/2.0. Ciągi te są zbieżne do
wspólnej granicy nazywanej średnią arytmetyczno-geometryczną. Napisać program wyznaczający średnią
arytmetyczno-geometryczną dwóch liczb.
"""
from math import sqrt

a0 = int(input("Enter a0: "))
b0 = int(input("Enter b0: "))
epsilon = 0.0000000001
while abs(a0 - b0) > epsilon:
    a1 = (a0 + b0) / 2
    b1 = sqrt(a0 * b0)
    a0 = (a1 + b1) / 2
    b0 = sqrt(a1 * b1)
print(a0)