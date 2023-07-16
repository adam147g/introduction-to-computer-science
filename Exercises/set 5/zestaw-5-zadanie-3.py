from random import randint


def is_check(data):
    for i in range(N):
        for j in range(i+1, N):
            if data[i][0] == data[j][0] or data[i][1] == data[j][1]:
                return False
            elif abs(data[i][0] - data[j][0]) == abs(data[i][1]-data[j][1]):
                return False
    return True


N = int(input("Podaj zakres hetmanów: "))
data = [(randint(0, 9), randint(0, 9)) for _ in range(N)]
chessboard = [[(" ", " ") for _ in range(10)] for x in range(10)]

for d in data:
    chessboard[d[0]][d[1]] = (str(d[0]), str(d[1]))

for box in chessboard:
    print(box)

print(is_check(data))
