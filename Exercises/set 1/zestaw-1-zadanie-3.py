a, b = 1, 1
x = int(input("Podaj x: "))
if x == 0 or x == 1 or x == 2:
    print(True)
    exit(0)
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
            print(True)
            exit(0)
print(False)
