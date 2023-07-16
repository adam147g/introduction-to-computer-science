"""
Kwadrat jest opisywany czwórką liczb całkowitych (x[1], x[2], y[1], y[2]), gdzie x[1], x[2],
y[1], y[2] oznaczają proste ograniczające kwadrat x[1] < x[2], y[1] < y[2]. Dana jest tablica
T zawierająca opisy N kwadratów. Proszę napisać funkcję, która zwraca wartość logiczną True,
jeśli w danej tablicy można znaleźć 13 nienachodzących na siebie kwadratów, których suma pól
jest równa 2012 i False w przeciwnym przypadku.
"""


def square_collision(check_list):
    for i in range(len(check_list) - 1):
        s1_x1, s1_x2, s1_y1, s1_y2 = check_list[i]
        s2_x1, s2_x2, s2_y1, s2_y2 = check_list[len(check_list) - 1]
        if not (s1_x1 > s2_x2 or s1_x2 < s2_x1 or s1_y1 > s2_y2 or s1_y2 < s2_y1 or
                (s1_x2 > s2_x2 and s1_x1 < s2_x1 and s1_y1 < s2_y1 and s1_y2 > s2_y2)):
            return True
    return False


def new_arguments(T, i):
    new_x1 = T[i][0]
    new_x2 = T[i][1]
    new_y1 = T[i][2]
    new_y2 = T[i][3]
    return new_x1, new_x2, new_y1, new_y2


def summary_square(arguments):
    return abs(arguments[1] - arguments[0]) * abs(arguments[3] - arguments[2])


def non_overlapping_squares(T, area=0, idx=0, squares=[]):
    if square_collision(squares) or area > 2012:
        return False
    if len(squares) == 13:
        if area == 2012:
            return True
        return False
    for i in range(idx, len(T)):
        arguments = new_arguments(T, i)
        if non_overlapping_squares(T, area + summary_square(arguments), i, squares + [arguments]):
            return True
    return False


T = [(87, 27, 41, 90), (13, 53, 10, 18), (2, 55, 8, 91), (81, 3, 60, 90),
     (78, 86, 54, 70), (96, 22, 17, 87), (90, 45, 37, 95), (54, 80, 40, 81),
     (51, 46, 70, 83), (23, 36, 10, 57), (23, 11, 20, 22), (97, 74, 86, 14),
     (68, 68, 69, 49), (85, 48, 18, 88), (24, 80, 84, 67), (47, 8, 72, 80),
     (22, 95, 50, 2), (35, 64, 7, 41), (73, 79, 40, 54), (43, 64, 77, 25)]
print(non_overlapping_squares(T))