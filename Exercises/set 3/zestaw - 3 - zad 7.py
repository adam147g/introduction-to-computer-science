from random import randint
N = int(input(">> "))
t = [randint(0, 1000) for _ in range(N)]
s = 0
print(t)
for i in range(N):
    while t[i]>0:
        if t[i] % 2 == 1:
            t[i] //= 10
            if t[i]==0:
                s += 1
        else:
            break
    if s>0:
        print("istnieje, indeks",i)
        break
