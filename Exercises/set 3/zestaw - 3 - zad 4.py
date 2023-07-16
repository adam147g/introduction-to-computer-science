# Stała e z dokładnością do N
N = int(input("N = "))
e, n = 0, 10 ** N
tab = []


def silnia(x):
    a = 1
    for i in range(1, x):
        a = a * i
    x = a
    return x

# dla i==0
e += n//1

silniai=1
for i in range(1, n):
    # silniai = silnia(i)
    silniai *= i
    if (n // silniai <= 1):
        break
    e = n // silniai + e

for o in range(N + 1):
    a = e % 10
    tab.append(a)
    e = e // 10
print(tab[N], end=",")
for o in range(2, N + 2):
    print(tab[N + 1 - o], end="")
