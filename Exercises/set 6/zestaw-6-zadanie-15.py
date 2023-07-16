#zadanie 15
#Problem 8 hetmanów

def func(N):
    tab_pos = [-1 for _ in range(N)]        # indeks to wiersz, wartość to kolumna ustawienia hetmana
                                            # hetman stoi pod (i,tab_pos[i])
    t0 = [False for _ in range(N)]          # do sprawdzania szachowania na kolumnach
    t1 = [False for _ in range(N * 2 - 1)]  # do sprawdzania szachowania na przekątnych - prawa góra,
                                            # bo wiersz + kolumna = const. dla jakiejś przekątnej
    t2 = [False for _ in range(N * 2 - 1)]  # do sprawdzania szachowania na przekątnych w drugą stronę - prawy dół,
                                            # bo wiersz - kolumna = const. dla jakiejś przekątnej
                                            # aby wiersz - kolumna > 0 dajemy: N-1 + wiersz - kolumna
    '''
    zamiast exit(0) można
    stop = False
    '''
    def queen(r, c):
        '''
        nonlocal stop
        '''
        if r == N:
            printing(tab_pos)
            '''
            stop = True
            '''
            exit(0)     # zeby nie wypisywać wszystkich rozwiązań, a tylko jedno
        else:
            if t0[c] or t1[r + c] or t2[N - 1 + r - c]:   # jeśli się szachują (nie mogę wstawić), to...
                return
            # else:
            tab_pos[r] = c                                  # to już gdy mogę wstawić
            t0[c] = t1[r + c] = t2[N - 1 + r - c] = True
            for i in range(N):
                queen(r + 1, i)
            '''
            for i in range(N):
                if stop:
                    return
                queen(r + 1, i)
            '''
            t0[c] = t1[r + c] = t2[N - 1 + r - c] = False   # wycofanie ruchu, gdy z pętli nie weszliśmy głębiej

    for i in range(N):
        queen(0, i)


def printing(tab):
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i] == j:
                print('X ', end='')
            else:
                print("~ ", end='')
        print()

    # print(tab)

print(func(8))



'''


def is_move_possible(T, row, column):
    for i in range(len(T)):
        if T[row][i] == 1:
            return False
    for j in range(len(T)):
        if T[j][column] == 1:
            return False
    for k in range(len(T)):
        for m in range(len(T)):
            if T[k][m] == 1:
                if abs(k - row) == abs(m - column):
                    return False
    return True


def chess_queen(T):
    T_len = len(T)
    for i in range(T_len):
        for j in range(T_len):
            if T[i][j] == 0:
                if is_move_possible(T, i, j):
                    T[i][j] = 1
                    chess_queen(T)
                    if sum(sum(a) for a in T) == T_len:
                        return T
                    T[i][j] = 0
    return T


T = [[0 for _ in range(8)] for i in range(8)]
print(chess_queen(T))
'''
