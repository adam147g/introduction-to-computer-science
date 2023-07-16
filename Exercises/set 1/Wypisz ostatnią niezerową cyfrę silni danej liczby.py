N = int(input("N="))
a=1
for i in range(N):
    a *= (i + 1)
while True:
    if a % 10 == 0:
        a //= 10
    if a % 10 != 0:
        print(a % 10)
        break

