"""
W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla nałożono
dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby
na polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do
obranego celu (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu.
Dana jest globalna tablica T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę.
Lewy górny narożnik ma współrzędne w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może
dostać się z pola w,k do prawego dolnego narożnika.
"""

def distance(T, x, y):
    return abs(len(T) - 1 - x) + abs(len(T) - 1 - y)


def chess_king(T, w, k, actual_distance,visited):
    global temporary
    visited.append((w, k))
    if w == (len(T) - 1) and k == (len(T) - 1):
        temporary = True
        print(visited)
        return
    new_rows = [-1,-1,-1,0,0,+1,+1,+1]
    new_cols = [-1,0,+1,-1,+1,-1,0,+1]
    for i in range(len(new_cols)):
        if not temporary:
            if w + new_rows[i] <= len(T) - 1 and k + new_cols[i] <= len(T) - 1 and w + new_rows[i] >= 0 and k + new_cols[i] >= 0:
                if (w + new_rows[i],k + new_cols[i]) not in visited:
                    current_distance = distance(T, w + new_rows[i], k + new_cols[i])
                    if current_distance < actual_distance and \
                            T[w][k] % 10 < T[w + new_rows[i]][k + new_cols[i]]//(10**(len(str(T[w + new_rows[i]][k + new_cols[i]]))-1)):
                        chess_king(T, w + new_rows[i], k + new_cols[i], current_distance,visited)
    if not temporary:
        for i in range(len(new_cols)):
            if not temporary:
                if w + new_rows[i] <= len(T) - 1 and k + new_cols[i] <= len(T) - 1 and w + new_rows[i] >= 0 and k + new_cols[i] >= 0:
                    if (w + new_rows[i],k + new_cols[i]) not in visited:
                        current_distance = distance(T, w + new_rows[i], k + new_cols[i])
                        if current_distance == actual_distance and \
                                T[w][k] % 10 < T[w + new_rows[i]][k + new_cols[i]]//(10**(len(str(T[w + new_rows[i]][k + new_cols[i]]))-1)):
                            chess_king(T, w + new_rows[i], k + new_cols[i], current_distance,visited)


w, k = 0, 0
T = [[21, 464, 992, 536, 971, 943, 324, 325],
    [361, 820, 378, 967, 415, 165, 516, 17],
    [409, 583, 608, 91, 991, 267, 531, 518],
    [643, 878, 527, 60, 593, 195, 479, 382],
    [444, 260, 152, 928, 731, 200, 981, 271],
    [115, 294, 715, 74, 133, 198, 447, 391],
    [505, 815, 317, 954, 877, 854, 154, 626],
    [463, 91, 732, 456, 360, 359, 352, 850]]

'''T=[[2, 30,40, 0 ],
   [0, 10, 0 ,0],
   [10,0,  0, 0],
   [10,10,10,10]]'''
for i in range(len(T)):
    print(T[i])
print()
actual_distance = abs(len(T) - 1 - w) + abs(len(T) - 1 - k)
temporary = False
chess_king(T, 0, 0, actual_distance, [])
print()
print(temporary)