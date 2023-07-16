# Na szachownicy o wymiarach N × N wypełnionej liczbami naturalnymi > 1 odbywają się wyścigi
# wież. Pierwsza wieża startuje z lewego górnego rogu i ma dotrzeć do prawego dolnego rogu
# szachownicy. Pierwsza wieża może wykonywać tylko ruchy w prawo lub w dół szachownicy. Druga wieża
# startuje z prawego górnego rogu i ma dotrzeć do lewego dolnego rogu szachownicy. Druga wieża
# może wykonywać tylko ruchy w lewo lub w dół szachownicy. Wygrywa wieża, która dotrze do mety
# w mniejszej liczbie ruchów. Wieże mogą wykonać ruch z jednego pola na drugie tylko wtedy, gdy
# liczby na obu polach są względnie pierwsze.
# Proszę napisać funkcję, która dla danej tablicy zwraca numer wieży, która wygra wyścig lub 0, jeżeli
# wyścig będzie nierozstrzygnięty. Można założyć, że podczas wyścigu wieże nie spotkają się na jednym
# polu. Po wykonaniu funkcji zawartość tablicy nie może ulec zmianie.

def NWD(number1, number2):
    while number2 != 0:
        c = number1 % number2
        number1 = number2
        number2 = c
    if number1 == 1:
        return True
    return False


def race(T):
    def rek(T, row, col, finish_row, finish_col, wspolczynnik):
        if row == finish_row and col == finish_col:
            return 0
        count = 10000
        for i in range(row, finish_row + 1):
            if NWD(T[row][col], T[i][col]):
                count = min(count, 1 + rek(T, i, col, finish_row, finish_col, wspolczynnik))
        for i in range(col, finish_col + wspolczynnik, wspolczynnik):
            if NWD(T[row][col], T[row][i]):
                count = min(count, 1 + rek(T, row, i, finish_row, finish_col, wspolczynnik))
        return count

    count_1 = rek(T, 0, 0, len(T) - 1, len(T) - 1, 1)
    count_2 = rek(T, 0, len(T) - 1, len(T) - 1, 0, -1)
    if count_1 > count_2:
        return 2, count_1, count_2
    if count_1 < count_2:
        return 1, count_1, count_2
    return 'tie', count_2, count_1


T = [[13, 2, 2, 2, 2, 13],
     [2, 2, 2, 2, 2, 2],
     [2, 2, 2, 2, 2, 11],
     [2, 2, 2, 2, 2, 2],
     [2, 2, 2, 2, 2, 2],
     [9, 2, 2, 2, 8, 13]]
print(race(T))
