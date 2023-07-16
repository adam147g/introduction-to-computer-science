a = int(input("a= "))
c = 1
s = c
while a > 0:
    b = a - 1
    while b > 0:
        print(" ", end="")
        b -= 1
    while c > 0:
        print("*", end="")
        c -= 1
    print("")
    c = s + 2
    s = s + 2
    a -= 1
