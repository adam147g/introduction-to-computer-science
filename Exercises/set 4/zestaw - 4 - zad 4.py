from random import randint

'''def just_definition(N):
    justList = [[randint(1, 10000) for _ in range(N)] for _ in range(N)]
    print(justList)
    count = 0
    maximum = 0
    column = 0
    row = 0
    for j in range(N):
        for i in range(N):
            count += justList[i][j]
        for x in range(N):
            maxNumber = count/justList[x][j]
            if maxNumber > maximum:
                maximum = maxNumber
                column = x
                row = j
        count = 0
    return maximum, column, row

print(just_definition(4))'''


def zad4(N):
    T = [[randint(1, 1000) for _ in range(N)] for _ in range(N)]
    sum_col = []
    sum_row = []
    for x in range(N):
        print(T[x])
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += T[i][j]
        sum_row.append(sum)

    for i in range(N):
        sum = 0
        for j in range(N):
            sum += T[j][i]
        sum_col.append(sum)

    max = 0
    max_col = None
    max_row = None
    for i in range(N):
        if sum_col[i]>max:
            max=sum_col[i]
            max_col=i

    max=100000000
    for i in range(N):
        if sum_row[i]<max:
            max=sum_row[i]
            max_row=i

    print()
    print(sum_col, sum_row)
    return sum_col[max_col]/sum_row[max_row], max_col, max_row


print(zad4(5))
