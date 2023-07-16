"""
Dana jest tablica T[N] wypełniona niepowtarzającymi się liczbami naturalnymi. Proszę zaimplementować
funkcję trojki(T) która zlicza wszystkie trójki liczb, które spełniają następujące warunki:
(1) największym wspólnym dzielnikiem trzech liczb jest liczba 1,
(2) pomiędzy dwoma kolejnymi elementami trójki może być co najwyżej jedna przerwa.
Funkcja powinna zwrócić liczbę znalezionych trójek.
Przykładowe wywołania funkcji:
print(trojki([2,4,6,7,8,10,12])) # 0 trójek
print(trojki([2,3,4,6,7,8,10])) # 1 trójka (3,4,7)
print(trojki([2,4,3,6,5])) # 2 trójki (2,3,5),(4,3,5)
print(trojki([2,3,4,5,6,8,7])) # 5 trójek (2,3,5),(3,4,5),(3,5,8),(5,6,7),(5,8,7)
"""


def NWD(number1, number2):
    while number2 != 0:
        c = number1 % number2
        number1 = number2
        number2 = c
    return number1


def trojki(T):
    n = len(T)
    suma = 0
    for i in range(n - 2):
        for j in range(i + 1, i + 3):
            for k in range(j + 1, j + 3):
                if j < n and k < n and \
                        NWD(T[i], T[j]) == NWD(T[j], T[k]) == NWD(T[i], T[k]) == 1:
                    suma += 1
    return suma


print(trojki([2, 4, 6, 7, 8, 10, 12]))  # 0 trójek
print(trojki([2, 3, 4, 6, 7, 8, 10]))   # 1 trójka (3,4,7)
print(trojki([2, 4, 3, 6, 5]))          # 2 trójki (2,3,5),(4,3,5)
print(trojki([2, 3, 4, 5, 6, 8, 7]))    # 5 trójek (2,3,5),(3,4,5),(3,5,8),(5,6,7),(5,8,7)
