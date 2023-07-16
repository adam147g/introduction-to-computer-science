"""
Dane jest słowo składające się z liter alfabetu angielskiego. Słowo to tniemy na kawałki, tak aby każdy
kawałek zawierał dokładnie jedną samogłoskę. Proszę napisać funkcję cutting(s), która zwraca liczbę
sposobów pocięcia słowa na kawałki.
Przykłady:
print(cutting(’student’)) # wypisze 2 bo stu-dent, stud-ent
print(cutting(’sesja’)) # wypisze 3 bo se-sja, ses-ja, sesj-a
print(cutting(’ocena’)) # wypisze 4 bo o-ce-na, o-cen-a, oc-e-na, oc-en-a,
print(cutting(’informatyka’)) # wypisze 36
"""

def ile_samoglosek(s):
    t = ['e', 'i', 'a', 'o', 'u', 'y']
    count = 0
    for x in s:
        if x in t:
            count += 1
    return count

def cutting(s):
    count = 0
    def rek(s):
        nonlocal count
        i = 1
        while i < len(s):
            samog_do_i = ile_samoglosek(s[:i])
            samog_od_i = ile_samoglosek(s[i:])
            if samog_do_i == 1:
                if samog_od_i == 1:
                    count += 1
                if samog_od_i > 1:
                    rek(s[i:])
            if samog_od_i == 0:
                break
            i += 1
    rek(s)
    return count




print(cutting('student'))       # wypisze 2 bo stu-dent, stud-ent
print(cutting('sesja'))         # wypisze 3 bo se-sja, ses-ja, sesj-a
print(cutting('ocena'))         # wypisze 4 bo o-ce-na, o-cen-a, oc-e-na, oc-en-a,
print(cutting('informatyka'))   # wypisze 36
