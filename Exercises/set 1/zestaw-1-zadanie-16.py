"""
Dany jest ciąg określony wzorem: A[n+1] = (A[n] % 2) ∗ (3 ∗ A[n] + 1) + (1 − A[n] % 2) ∗ A[n] / 2.
Startując z dowolnej liczby naturalnej > 1 ciąg ten osiąga wartość 1. Napisać program, który
znajdzie wyraz początkowy z przedziału 2-10000 dla którego wartość 1 jest osiągalna po największej
liczbie kroków.
"""
a0 = 2
m = 1

for a0 in range(2, 10000):
    n = 0
    while a0 != 1:
        a0 = (((a0 % 2) * (3 * a0 + 1)) + ((1 - (a0 % 2)) * (a0 / 2)))
        n += 1
    if n > m:
        m = n
print(m)