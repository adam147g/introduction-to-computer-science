# zad 6
acc = 0.00001
a = 0
b = 5                   # bo 5^5 wiem, że > 2020
while (b - a > acc):
    x = (a + b) / 2
    if (x ** x > 2020):
        b = x
    else:
        a = x
print(x)
