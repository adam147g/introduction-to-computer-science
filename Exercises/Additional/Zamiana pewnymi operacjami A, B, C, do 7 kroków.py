# Bit algo
# Zamiana pewnymi operacjami A, B, C, do 7 kroków

def A(x):
    last_digit = x % 10
    second_digit = (x % 100) // 10

    x = x - last_digit - second_digit * 10
    x = x + second_digit + last_digit * 10
    return x


def B(x):
    return x * 3


def C(x):
    num = 1
    while 10 ** num < x:
        num += 1
    num -= 1
    first_digit = (x // 10 ** (num))
    x -= first_digit * 10 ** num
    return x


def transform(x, y, steps_remain=7, result=''):
    if steps_remain == -1:
        return False
    if x == y:
        print(result)
        return True

    if transform(B(x), y, steps_remain - 1, result + 'B'):
        return True
    if x >= 10:
        if transform(A(x), y, steps_remain - 1, result + 'A'):
            return True
        if transform(C(x), y, steps_remain - 1, result + 'C'):
            return True


x = int(input())
y = int(input())
print(transform(x, y))