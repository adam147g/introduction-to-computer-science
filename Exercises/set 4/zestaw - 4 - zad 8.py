"""
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która poszukuje
w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku prawo-dół, liczącego
co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić informacje
czy udało się znaleźć taki ciąg oraz długość tego ciągu.
"""


def the_longest_geometric_sequence_diagonally(T):
    longest_sequence = 0
    for i in range(len(T) - 2):
        for j in range(len(T) - 2):
            actual_sequence = 2
            first = T[i][j]
            second = T[i + 1][j + 1]
            quotient = second / first
            k, m = i + 2, j + 2
            flag = True
            while k < len(T) and m < len(T) and flag:
                flag = False
                if T[k - 1][m - 1] * quotient == T[k][m]:
                    flag = True
                    actual_sequence += 1
                    k += 1
                    m += 1
            longest_sequence = max(longest_sequence, actual_sequence)
    if longest_sequence > 2:
        return True, longest_sequence
    return False, 0


T = [[1 , 2,  2, 8, 14],
     [12, 2,  4, 5, 1 ],
     [2 , 1,  5, 8, 17],
     [11, 3,  2, 1, 16],
     [3 , 15, 3, 3, 7 ]]
print(the_longest_geometric_sequence_diagonally(T))