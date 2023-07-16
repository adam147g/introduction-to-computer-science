possib = ["I", 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]


def find_idx(x, tab):
    for i in range(len(tab)):
        if tab[i] == x:
            return i
    return None


def change_1(x):
    if len(x) > 0:
        sum = 0
        first = find_idx(x[0], possib)
        if 1 < len(x):
            if first < find_idx(x[1], possib):
                sum += values[find_idx(x[0] + x[1], possib)]
                sum += change_1(x[2:])
            else:
                sum += values[first]
                sum += change_1(x[1:])
        else:
            sum += values[first]
        return sum
    return 0


def change_2(x, sum=0):
    if len(x) > 0:
        first = find_idx(x[0], possib)
        if 1 < len(x):
            if first < find_idx(x[1], possib):
                return change_2(x[2:], sum + values[find_idx(x[0] + x[1], possib)])
            else:
                return change_2(x[1:], sum + values[first])
        else:
            return change_2('', sum + values[first])
    return sum


T = ['MMXXII', 'MCMLIX', 'MMCDXXIV']
for x in T:
    print(x, "-", change_1(x),"-", change_2(x))
