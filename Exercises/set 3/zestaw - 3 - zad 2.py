x = int(input("x: "))
y = int(input("y: "))
if len(str(x)) != len(str(y)):  # to można ominąć - celem jest tylko instant wykluczenie
    print(False)
l_x = [0] * 10
l_y = [0] * 10
while x != 0:
    l_x[x % 10] += 1
    x //= 10
    l_y[y % 10] += 1
    y //= 10
if l_x == l_y:
    print(True)
else:
    print(False)