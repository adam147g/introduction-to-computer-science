from random import randint
N = int(input(">> "))
t = [randint(0, 1000) for _ in range(N)]
s = 0
print(t)
for i in range(N):
    while t[i]>0:
        if t[i] % 2 == 0: t[i] //= 10
        else:
            s += 1
            break

if s == N: print("tak")
else: print("nie")