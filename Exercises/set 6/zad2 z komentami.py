# program dzieli słowo na kawałki posiadające co najmniej jedną samogłoske za pomocą rekurencji
def czysamogloska(litera):
    return litera in ["a", "e", "i", "o", "u", "y"]


def cutting(s, k=0):
    if (s == ""):
        if (k > 1):
            return 1
        else:
            return 0
    sam = 0
    i = 0
    suma = 0

    while (i < len(s)):
        if (czysamogloska(s[i])):
            sam += 1
        if (sam > 0):
            suma = suma + cutting(s[i + 1:], k + 1)
        i += 1
    return suma


print(cutting("lambada"))
