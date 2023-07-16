import math

def pierwsza(a):
    if a == 2 or a == 3:
        return True
    elif a < 2 or a % 2 == 0 or a % 3 == 0:
        return False
    else:
        i = 5
        while i <= math.sqrt(a):
            if a % i == 0:
                return False
            i += 2
            if a % i == 0:
                return False
            i += 4
        return True

def rek(n, result=0, pos=0, b=False):
    if n == 0:
        if result > 9 and b and pierwsza(result):
            print(result)
    else:
        rek(n // 10, result, pos, True)
        rek(n // 10, result + ((n % 10) * (10 ** pos)), pos + 1, b)

rek(123)
print()
rek(14357)