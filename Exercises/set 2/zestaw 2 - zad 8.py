"""
Pewnych liczb nie można przedstawić jako sumy elementów spójnych fragmentów ciągu Fibonacciego,
np. 9, 14, 15, 17, 22. Proszę napisać program, który wczytuje liczbę naturalną n, wylicza i wypisuje
następną taką liczbę większą od n. Można założyć, że 0 < n < 1000.
"""
def f(x):                               # f - czy_istnieje_suma_elementów_spójnych_fragmentów_ciągu_Fibonacciego
    a, b = 1, 1
    if x == 0 or x == 1 or x == 2:
        return True
    else:
        while a + b <= x:
            b = a + b
            a = b - a
            a_ = a
            b_ = b
            sum = 0
            while (sum < x and b_ > 0):
                sum += b_
                a_ = b_ - a_
                b_ = b_ - a_
            if sum == x:
                return True
    return False

num=int(input(">> "))
num+=1
while f(num):
    num+=1
print(num)