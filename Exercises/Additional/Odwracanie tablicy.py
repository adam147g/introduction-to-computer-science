# Bit algo
# Odwracanie tablicy

def reverse(a, i=0):
    if i >= len(a) // 2:
        return
    a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]
    reverse(a, i + 1)


a = [1, 2, 4, 7, 2, 7]
reverse(a)
print(a)
