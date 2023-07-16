# Dwie liczby naturalne są czynnikowo-podobne, jeżeli w swoich rozkładach na czynniki pierwsze mają
# dokładnie jeden czynnik równy. Na przykład: 24 i 14 albo 32 i 18. Dana jest tablica T[N][N]
# zawierająca liczby naturalne. Dwie liczby sąsiadują ze sobą wtedy, gdy leżą w sąsiednich kolumach i
# sąsiednich wiersza. Proszę napisać funkcję three(T), która zwraca ilość liczb w tablicy sąsiadujących
# dokładnie z 3 liczbami czynnikowo-podobnymi.

def is_good(x, y):
    i = 2
    count = 0
    while i <= min(x, y):
        if x % i == 0 and y % i == 0:
            count += 1
            x //= i
            y //= i
            i -= 1
        i += 1
        if count > 1:
            return 0
    if count == 1:
        return 1
    return 0


def zad(T):
    count = 0
    row = [-1, 0, 1, -1, 1, -1, 0, 1]
    col = [-1, -1, -1, 0, 0, 1, 1, 1]
    for i in range(len(T)):
        for j in range(len(T)):
            curr = 0
            for x in range(len(row)):
                if len(T) > i + row[x] > -1 and len(T) > j + col[x] > -1:
                    curr += is_good(T[i][j], T[i + row[x]][j + col[x]])
            if curr == 3:
                count += 1
                print(i, j)

    return count


T = [[24,14,24,10],
     [0, 24, 0, 9],
     [0, 0, 3, 6],
     [0, 0, 0, 0]]
print(zad(T))
