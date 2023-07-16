# zadanie 3
from random import randint
from math import inf

# def zad3(t, k):
#     def rek(t, k, cost=0, w=-1):
#         if w == -1: return rek(t, k, t[0][k], 0)
#         if w == 7: return cost
#         if k == 0: return min(rek(t, 0, cost + t[w + 1][0], w + 1), rek(t, 1, cost + t[w + 1][1], w + 1))
#         if k == 7: return min(rek(t, 7, cost + t[w + 1][7], w + 1), rek(t, 6, cost + t[w + 1][6], w + 1))
#         return min(rek(t, k - 1, cost + t[w + 1][k - 1], w + 1), rek(t, k, cost + t[w + 1][k], w + 1),
#                    rek(t, k + 1, cost + t[w + 1][k + 1], w + 1))                                              #to jest taki else
#
#     # end def
#     return rek(t, k)
#
# # end def

def rek(t, k, w=0):
    if k < 0 or k > 7:
        return inf
    if w == 7:
        return t[w][k]
    return min(rek(t, k - 1, w + 1), rek(t, k, w + 1), rek(t, k + 1, w + 1)) + t[w][k]


t = [[randint(1, 3) for _ in range(8)] for _ in range(8)]

for x in range(len(t)):
    for y in range(len(t)):
        print(t[x][y], end=" ")
    print()

print(rek(t, 7))
