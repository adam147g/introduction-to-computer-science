"""
Dany jest zbiór punktów leżących na płaszczyźnie opisany przy pomocy struktury
dane = [(x[1], y[1]), (x[2], y[2]), (x[3], y[3]), ..., (x[N], y[N])] Proszę napisać funkcję, która
zwraca wartość True jeżeli zbiorze istnieją 4 punkty wyznaczające kwadrat o bokach równoległych
do osi układu współrzędnych, a wewnątrz tego kwadratu nie ma żadnych innych punktów. Do funkcji
należy przekazać strukturę opisującą położenie punktów.
"""

# nawet mi się nie chce tego sprawdzać :D

from random import randint


def find_square(data):
    for i in range(len(data)):
        for j in range(1, 10 - i):
            try:
                if data[i][1] == data[i + j][1]:
                    A = data[i]
                    B = data[i + j]
                    side = abs(data[i][0] - data[i + j][0])
                    for k in range(len(data)):
                        if (data[i + j][0] == data[k][0]) and \
                                (abs(data[i + j][1] - data[k][1]) == side):
                            C = data[k]
                            for m in range(len(data)):
                                if data[k][1] == data[m][1] and \
                                        abs(data[m][0] - data[k][0]) == side:
                                    if data[m][0] == data[i][0] and \
                                            abs(data[m][1] - data[i][1]) == side:
                                        D = data[m]
                                        if A[0] == D[0] and A[1] == B[1] and \
                                                B[0] == C[0] and C[1] == D[1] and \
                                                A[1] != C[1] and A[0] != C[0]:
                                            for a in range(data[i + 1][0], data[i + j + 1][0]):
                                                if data[a][0] not in data:
                                                    continue
                                                else:
                                                    break
                                            for b in range(data[i + 1][1], data[m + 1][1]):
                                                if data[b][1] not in data:
                                                    continue
                                                else:
                                                    break
                                            return A, B, C, D
            except IndexError:
                return False
    return False


N = 100
data = [(randint(0, 15), randint(0, 15)) for _ in range(N)]
print(find_square(data))