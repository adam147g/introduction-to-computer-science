from random import randint


def just_definition(N):
    justList = [[randint(-100, 100) for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            print("|", justList[i][j], end="\t")
        print("|")

    count = 0
    maximum = 0
    column = 0
    row = 0
    for j in range(N):
        for i in range(N):
            count += justList[i][j]
        for x in range(N):
            if justList[x][j] == 0:
                continue
            else:
                maxNumber = count / justList[x][j]
                if maxNumber > maximum:
                    maximum = maxNumber
                    column = x
                    row = j
        count = 0
    return maximum, column, row


print(just_definition(4))
