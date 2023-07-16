from random import randint

# da się szybciej, ale nie chce mi się modyfikować kodu

def just_definition(t):
    len_t = len(t)
    result = 0
    minimumValue = x+1
    for i in range(len_t):
        if t[i] < minimumValue:
            minimumValue = t[i]
        else:
            continue
    for k in range(len_t):
        if t[k] == minimumValue:
            result += 1
    if result > 1:
        return False
    else:
        return True, minimumValue

n = int(input("Podaj zakres tablicy: "))
x = int(input("Podaj maksymalną wartość tablicy: "))
t = [randint(-abs(x), abs(x)) for _ in range(n)]
print(t)
print(just_definition(t))