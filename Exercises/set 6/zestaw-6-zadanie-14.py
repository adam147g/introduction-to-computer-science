"""
Problem wież w Hanoi (treść oczywista).
"""


def hanoi_tower(n, result):
    result[0] += 1
    if n == 1:
        return
    hanoi_tower(n - 1, result)
    hanoi_tower(n - 1, result)
    return result[0]


result = [0]
print(hanoi_tower(3, result))

# 2ND SOLUTION - WITH GLOBAL PARAMETERS

def hanoi_tower_global(n):
    global result_glob
    result_glob += 1
    if n == 1:
        return
    hanoi_tower_global(n - 1)
    hanoi_tower_global(n - 1)
    return result_glob


result_glob = 0
print(hanoi_tower_global(3))