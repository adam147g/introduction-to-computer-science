"""
Tablica T = [(x1, y1), (x1, y1), ...] zawiera położenia N punktów o współrzędnych opisanych
wartościami typu float. Proszę napisać funkcję, która zwróci najmniejszą odległość między
środkami ciężkości 2 niepustych podzbiorów tego zbioru.
"""
from math import sqrt, inf


def centre_of_mass(array, length):
    center1_x = center1_y = 0
    for i in range(len(array)):
        center1_x += array[i][0]
        center1_y += array[i][1]
    return center1_x / length, center1_y / length


def calculate_distance(x, y):
    distance_x = abs(x[0] - y[0])
    distance_y = abs(x[1] - y[1])
    total_distance = sqrt(distance_x ** 2 + distance_y ** 2)
    return total_distance


def the_lowest_subset(T, array_1, array_2, min_distance, position=0, l1=0, l2=0, taken=0):
    if position == len(T):
        return
    if taken == 0:
        array_1[position] = T[position]
    elif taken == 1:
        array_2[position] = T[position]
    if l1 >= 1 and l2 >= 1:
        center1 = centre_of_mass(array_1, l1)
        center2 = centre_of_mass(array_2, l2)
        actual_distance = calculate_distance(center1, center2)
        min_distance[0] = min(min_distance[0], actual_distance)
    the_lowest_subset(T, array_1, array_2, min_distance, position + 1, l1 + 1, l2, 0)
    the_lowest_subset(T, array_1, array_2, min_distance, position + 1, l1, l2 + 1, 1)
    the_lowest_subset(T, array_1, array_2, min_distance, position + 1, l1, l2, 2)
    if taken == 0:
        array_1[position] = (0, 0)
    elif taken == 1:
        array_2[position] = (0, 0)


T = [(47, 29), (74, 56), (69, 32), (67, 85), (72, 42), (6, 62), (80, 64), (13, 1), (5, 69), (98, 42)]
array_1 = [(0, 0) for _ in range(len(T))]
array_2 = [(0, 0) for _ in range(len(T))]
min_distance = [inf]
the_lowest_subset(T, array_1, array_2, min_distance)
print(min_distance[0])