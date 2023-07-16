"""
Napisać program wyznaczający wartość liczby e korzystając z zależności: e = 1/0! + 1/1! + 1/2! + 1/3! + ...
"""

n = 1
e = 1
for i in range(1, 30):
    n = n*i
    e = 1/n + e
    i += 1
print("e =", e)
