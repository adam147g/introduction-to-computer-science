"""
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która zwraca
liczbę par elementów, o określonym iloczynie, takich że elementy są odległe o jeden ruch skoczka szachowego.
"""
from random import randint


def knight_moves(array, i, x, y):
    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]
    new_x = x + x_move[i]
    new_y = y + y_move[i]
    if new_x >= 0 and new_y >= 0 and new_x < len(array) and new_y < len(array):
        return (new_x, new_y)
    return None


def knight_move(array, product):
    result = []
    for i in range(len(array)):
        for j in range(len(array)):
            for x in range(8):
                new_pos = knight_moves(array, x, j, i)
                if new_pos is not None:
                    if array[new_pos[0]][new_pos[1]] * array[i][j] == product:
                        if not (new_pos, (i, j)) in result:
                            result.append(((i, j), new_pos))
    return result


N = 5
product = 12
array = [[randint(1, 20) for _ in range(N)] for _ in range(N)]
for i in range(len(array)):
    print(array[i])
print(knight_move(array, product))
print()
array = [[1, 0, 0],
         [0, 2, 12],
         [0, 0, 6]]
for i in range(len(array)):
    print(array[i])
print(knight_move(array, product))
