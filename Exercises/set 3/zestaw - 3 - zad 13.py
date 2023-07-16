from random import randint

def zad13(t):
    max_len = 0
    len_t = len(t)
    begin = 0
    last = len_t - 1
    count = 0
    max_count = 0
    while begin < len_t:
        while last >= begin:
            if t[last] != t[begin]:
                last -= 1
            else:
                count += 1
                x = begin + 1
                y = last - 1
                while len_t > x > -1 and len_t > y > -1 and t[x] == t[y]:
                    count += 1
                    x += 1
                    y -= 1
                max_count = max(max_count, count)
                count = 0
                last -= 1
        begin += 1
        last = len_t - 1
    print(max_count)


n = int(input("Podaj wielkość tablicy: "))
T = [randint(1, 10) for _ in range(n)]
t = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]

print(t)
zad13(t)
print(T)
zad13(T)
