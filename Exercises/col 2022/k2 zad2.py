# W tablicy o rozmiarze N × N wypełnionej liczbami naturalnymi umieszczono dokładnie jeden fragment
# ciągu Fibonacciego o długości co najmniej 3 elementów. Cały fragment leży w jednym z wierszy
# lub kolumn w kierunku rosnącym lub malejącym. Prosze napisać funkcję, która dla zadanej tablicy
# odszuka ten fragment i zwróci jego wartość.

def kolejne(x, y):
    a = 1
    b = 1
    while a < x:
        b = a + b
        a = b - a
    if a == x and b == y:
        return True
    return False

# wiersze

def zad(T):
    def rek(T, row, col, bigger):
        nonlocal count, remember
        for i in range(col, len(T)):
            if kolejne(bigger, T[row][i]):
                count += 1
                remember = T[row][i]
                rek(T, row, i, T[row][i])

    for a in range(len(T)):
        count = 0
        for i in range(len(T)):
            for j in range(i, len(T)):
                if kolejne(T[a][i], T[a][j]):
                    count = 2
                    remember = T[a][j]
                    rek(T, a, j, T[a][j])
            if count > 2:
                return (count, remember)


T = [[8, 13, 3, 4, 5, 6, 7, 8, 9, 9, 9, 13],
     [8, 13, 3, 4, 5, 6, 7, 8, 9, 9, 9, 13],
     [8, 13, 3, 4, 5, 6, 7, 8, 9, 9, 9, 13],
     [8, 13, 3, 4, 5, 6, 7, 8, 9, 9, 9, 13],
     [8, 13, 3, 4, 5, 6, 7, 8, 9, 9, 9, 13],
     [8, 13, 3, 4, 5, 6, 7, 8, 9, 9, 9, 13],
     [8, 13, 3, 4, 5, 6, 7, 8, 9, 9, 9, 13],
     [8, 13, 3, 4, 5, 6, 7, 8, 9, 9, 9, 13],
     [8, 13, 3, 4, 5, 6, 7, 8, 9, 9, 9, 13],
     [8, 13, 3, 4, 5, 6, 7, 8, 9, 9, 9, 13],
     [8, 13, 3, 4, 5, 6, 7, 8, 9, 9, 9, 13],
     [8, 13, 3, 4, 5, 6, 7, 8, 9, 9, 9, 13]]
print(zad(T))
