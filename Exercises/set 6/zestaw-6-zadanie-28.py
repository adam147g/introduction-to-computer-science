"""
Dany jest zbiór N liczb naturalnych umieszczony w tablicy T[N]. Proszę napisać funkcję,
która zwraca informację, czy jest możliwy podział zbioru N liczb na trzy podzbiory, tak aby w każdym
podzbiorze, łączna liczba jedynek użyta do zapisu elementów tego podzbioru w systemie dwójkowym była
jednakowa. Na przykład: [2, 3, 5, 7, 15] → true, bo podzbiory {2,7} {3,5} {15} wymagają użycia 4 jedynek,
[5, 7, 15] → false, podział nie istnieje.
"""


def count_ones(x):
    count = 0
    while x > 0:
        if x % 2 == 1:
            count += 1
        x //= 2
    return count

def count_tab(T):
    count = 0
    for x in T:
        count += count_ones(x)
    return count

def divide(T, idx = 0, res_1 = [], res_2 = [], res_3 = []):
    if idx == len(T):
        if count_tab(res_1) == count_tab(res_2) == count_tab(res_3):
            print(res_1, res_2, res_3)
            return True
        return False
    res_1.append(T[idx])
    if divide(T, idx+1, res_1, res_2, res_3):
        return True
    else:
        res_1.remove(T[idx])
    res_2.append(T[idx])
    if divide(T, idx + 1, res_1, res_2, res_3):
        return True
    else:
        res_2.remove(T[idx])
    res_3.append(T[idx])
    if divide(T, idx + 1, res_1, res_2, res_3):
        return True
    else:
        res_3.remove(T[idx])
    return False


def fasterdivide(T, max, idx = 0, sum_1 = 0, sum_2 = 0, sum_3 = 0):
    if idx == len(T):
        if sum_1 == sum_2 == sum_3:
            return True
        return False
    if sum_1 > max or sum_2 > max or sum_3 > max:
        return False
    return (fasterdivide(T, max, idx + 1, sum_1 + count_ones(T[idx]), sum_2, sum_3) or
            fasterdivide(T, max, idx + 1, sum_1, sum_2 + count_ones(T[idx]), sum_3) or
            fasterdivide(T, max, idx + 1, sum_1, sum_2, sum_3 + count_ones(T[idx])))

T_1=[2, 3, 5, 7, 15]
T_2=[5, 7, 15]
print(T_1)
max_1 = count_tab(T_1)
if  max_1 % 3 == 0:
    print(divide(T_1))
    print(fasterdivide(T_1,max_1//3))
else:
    print(False)

print()
print(T_2)
max_2 = count_tab(T_2)
if max_2 % 3 == 0:
    print(divide(T_2))
    print(fasterdivide(T_2,max_2//3))
else:
    print(False)