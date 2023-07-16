"""
Dane jest słowo składające się z liter alfabetu angielskiego. Słowo to tniemy na co najmniej dwa kawałki,
tak aby każdy kawałek zawierał co najmniej jedną samogłoskę. Proszę napisać funkcję cutting(s), która
zwraca liczbę sposobów pocięcia słowa na kawałki.
Przykłady:
print(cutting(’student’)) # wypisze 2 bo stu-dent, stud-ent
print(cutting(’sesja’)) # wypisze 3 bo se-sja, ses-ja, sesj-a
print(cutting(’ocena’)) # wypisze 8 bo o-cena, o-ce-na, o-cen-a, oc-ena, oc-e-na,
oc-en-a, oce-na, ocen-a
"""

def czy_samogl(s):
    t = ['e', 'i', 'a', 'o', 'u', 'y']
    for x in s:
        if x in t:
            return 1
    return 0

def cutting(s):
    count = 0
    def rek(s):
        nonlocal count
        i = 1
        while i < len(s):
            samog_do_i = czy_samogl(s[:i])
            samog_od_i = czy_samogl(s[i:])
            if samog_do_i == 1:
                if samog_od_i == 1:
                    count += 1
                    rek(s[i:])
            if samog_od_i == 0:
                break
            i += 1
    rek(s)
    return count


print(cutting('student'))   # wypisze 2 bo stu-dent, stud-ent
print(cutting('sesja'))     # wypisze 3 bo se-sja, ses-ja, sesj-a
print(cutting('ocena'))     # wypisze 8 bo o-cena, o-ce-na, o-cen-a, oc-ena, oc-e-na, oc-en-a, oce-na, ocen-a