a, b = 1, 2
while a <= 2020:
    a = a + b
    b = a + b
x = a - 2020

if x % 2 == 0:
    a = 1 + x / 2
    b = 1 + x / 2
else:
    a = int(1 + x // 2)
    b = int(1 + x // 2 + 1)
print(a, b)
