# Bit ago
# Chodzenie po tablicy, po wyższych liczbach w pionie i poziomie
# tak aby wylądować na końcy tablicu z początku tablicy

def is_path(a, row, col):
    if row == len(a) - 1 and col == len(a) - 1:
        return True

    if row < len(a) - 1 and a[row + 1][col] > a[row][col]:
        if is_path(a, row + 1, col):
            return True

    if col < len(a) - 1 and a[row][col + 1] > a[row][col]:
        if is_path(a, row, col + 1):
            return True
    return False


a = [[0, 100, 100, 100],
     [1, 100, 100, 100],
     [2,  3,  100, 100],
     [3,  4,   5,   6]]

b = [[0,  100, 100, 100],
     [1,  100, 100, 100],
     [2,  100, 100, 100],
     [100, 4,   5,   6]]

def cos_tam(a):
    if is_path(a,0,0):
        print('There is away')
    else:
        print('-\_(0 0)_/-')
print()
print('Dla pierwszej tablicy')
cos_tam(a)
print()
print('Dla drugiej tablicy')
cos_tam(b)