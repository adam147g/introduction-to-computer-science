from math import pi

"""
Napisać program obliczający wartości cos(x) z rozwinięcia w szereg Maclaurina.

Z Maclaurina wiem, że cos(x) = x^0/(0!) - x^2/(2!) + x^4/(4!) - x^6/(6!)  + x^8/(8!) - ...
    x^0/(0!) = 1 - zawsze
"""
decision=input("Chcesz użyć wartości pi? - Pisać ")
if decision=="tak" or decision=="TAK":
    decision=pi
    x = float(input("napisz ile razy chcesz mnożyć pi "))
    x=decision*x
else:
    x = float(input("Podaj x: "))
x = (x % (2 * pi))

eps = 0.0000000000000001
sum = nast_wyraz = 1
potega = 2

while abs(nast_wyraz) > eps:
    nast_wyraz *= -(x ** 2) / ((potega - 1) * potega)
    sum += nast_wyraz
    potega += 2
if abs(sum)>1:
    print("ERROR")
    exit(0)
else:
    print(round(sum, 12))
