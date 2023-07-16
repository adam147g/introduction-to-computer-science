"""
Zadanie jak powyżej. Funkcja powinna dostarczyć drogę króla w postaci tablicy zawierającej
kierunki (liczby od 0 do 7) poszczególnych ruchów króla do wybranego celu.
"""


def first_digit(number):
    while number > 9:
        number //= 10
    return number


def king_recursion(T, w, k, visited=[]):
    visited.append((w, k))
    if ((w == len(T) - 1 and k == len(T) - 1) or (w == 0 and k == 0)
            or (w == 0 and k == len(T) - 1) or (w == len(T) - 1 and k == 0)):
        return True, visited
    w_move = [0, -1, -1, -1, 0, 1, 1, 1]
    k_move = [1, 1, 0, -1, -1, -1, 0, 1]
    for i in range(8):
        new_w = w + w_move[i]
        new_k = k + k_move[i]
        if new_w >= 0 and new_k >= 0 and new_w < len(T) and new_k < len(T):
            if (new_w, new_k) not in visited:
                first = first_digit(T[new_w][new_k])
                if first > T[w][k] % 10:
                    if king_recursion(T, new_w, new_k, visited):
                        return True, visited
    return False


T = [[30, 50, 49, 30, 49, 17, 39, 14],
     [33, 10, 50, 36, 26, 24, 34, 25],
     [19, 22, 9, 21, 47, 6, 19, 45],
     [15, 10, 42, 27, 21, 3, 20, 4],
     [7, 30, 6, 18, 13, 40, 46, 47],
     [21, 46, 50, 16, 10, 22, 32, 36],
     [11, 26, 43, 25, 24, 36, 24, 50],
     [40, 38, 40, 17, 36, 13, 38, 36]]
w, k = 3, 4
print(king_recursion(T, w, k))