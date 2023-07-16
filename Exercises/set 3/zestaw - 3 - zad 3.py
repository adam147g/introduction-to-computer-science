"""
MOJE ROZWIĄZANIE
def Sito_Eratostenesa(N):
    NList = list()
    while N > 1:
        NList.append(N)
        N -= 1
    for N in NList:
        if N % 2 == 0 and N != 2:
            NList.remove(N)
    for N in NList:
        if N % 3 == 0 and N != 3:
            NList.remove(N)
    for N in NList:
        if N % 5 == 0 and N != 5:
            NList.remove(N)
    for N in NList:
        if N % 7 == 0 and N != 7:
            NList.remove(N)
    return NList


N = int(input("Podaj liczbę: "))
print(Sito_Eratostenesa(N))
"""
# ROZWIĄZANIE NA ĆWICZENIACH
from math import sqrt
from math import ceil
N = int(input("Podaj liczbę: "))
tab = [True for _ in range(N+1)]
tab[0] = tab[1] = False
for i in range(2, ceil(sqrt(N)+1)):
    if tab[i]:
        for a in range(i*i, N+1, i):
            tab[a] = False
for i in range(N+1):
    if tab[i]:
        print(i)
