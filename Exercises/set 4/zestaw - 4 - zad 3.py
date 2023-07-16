from random import randint


def have_even(N):
    justList = [[randint(0, 100) for _ in range(N)] for _ in range(N)]
    count = 0
    print(justList)
    for i in range(N):
        for j in range(N):
            if justList[i][j] % 2 == 0:
                count += 1
            elif justList[i][j] % 2 != 0:
                while justList[i][j] > 0:
                    r = justList[i][j] % 10
                    justList[i][j] //= 10
                    if r % 2 == 0:
                        count += 1
                    else:
                        continue
        if count == N:
            return True
        else:
            continue
    return False


print(have_even(4))
