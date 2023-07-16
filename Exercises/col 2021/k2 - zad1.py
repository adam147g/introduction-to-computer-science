"""
Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami całkowitymi.
Proszę zaimplementować funkcję chess(T) która ustawia na szachownicy dwie wieże, tak aby suma liczb na
„szachowanych” przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna
zwrócić położenie wież w postaci krotki (row1, col1, row2, col2).
Uwaga: zakładamy, że pola na których znajdują się wieże nie są szachowane.

Przykładowe wywołania funkcji:
print(chess([[4,0,2],[3,0,0],[6,5,3]])) # (0,1,1,0) suma=17
print(chess([[1,1,2,3],[-1,3,-1,4], [4,1,5,4], [5,0,3,6]] # (2,3,3,1) suma=35
"""
def chess(T):
    n = len(T)
    sum_w = [0] * n
    sum_k = [0] * n
    for w in range(n):
        for k in range(n):
            sum_w[w] += T[w][k]
            sum_k[k] += T[w][k]

    max_sum = 0
    pos = ((-1, -1), (-1, -1))

    for w_1 in range(n):
        for k_1 in range(n):
            for w_2 in range(n):
                for k_2 in range(n):
                    if k_1 != k_2 and w_1 != w_2:
                        tmp = sum_w[w_1] + sum_k[k_1] - 2 * T[w_1][k_1] \
                            + sum_w[w_2] + sum_k[k_2] - 2 * T[w_2][k_2] \
                            - T[w_1][k_2] - T[w_2][k_1]
                        if max_sum < tmp:
                            max_sum = tmp
                            pos = ((w_1, k_1), (w_2, k_2))

    return pos




chess_1 = [[4,0,2],
           [3,0,0],
           [6,5,3]]         # ((0,1) ,(1,0)) suma=17

chess_2 = [[ 1, 1, 2, 3],
           [-1, 3,-1, 4],
           [ 4, 1, 5, 4],
           [ 5, 0, 3, 6]]   # ((2,3) ,(3,1)) suma=35
print(chess(chess_1))
print(chess(chess_2))

