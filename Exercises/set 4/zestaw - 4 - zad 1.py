N = 9
spiralList = [[0 for _ in range(N)] for __ in range(N)]
n = 1
dl = 0
wys = N-1
count = int((N+1)/2)
for i in range(count):
    for j in range(dl, wys+1):
        spiralList[i][j] = n
        n += 1
    for j in range(dl+1, wys+1):
        spiralList[j][wys] = n
        n += 1
    for j in range(wys - 1, dl-1, -1):
        spiralList[wys][j] = n
        n += 1
    for j in range(wys-1, dl, -1):           # j zmniejsza się od dl do wys-1 o 1
        spiralList[j][dl] = n
        n += 1
    dl += 1
    wys -= 1

for i in range(N):
    for j in range(N):
        print(spiralList[i][j], end="\t")    # \t czyli tab
    print()
