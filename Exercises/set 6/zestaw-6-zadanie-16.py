"""
Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą liczbę samogłosek
oraz sumy kodów ascii liter z których są zbudowane są identyczne, na przykład "ula" → 117, 108, 97
oraz "exe" → 101, 120, 101. Proszę napisać funkcję word(s1, s2), która sprawdza czy jest możliwe
zbudowanie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. Dodatkowo funkcja
powinna wypisać znaleziony wyraz.
"""


def count_vowels(string):
    count = 0
    for i in range(len(string)):
        s = string[i]
        if s == "a" or s == "e" or s == "i" or s == "o" or s == "u" or s == "y":
            count += 1
    return count


def ascii_sum(string):
    count = 0
    for i in range(len(string)):
        count += ord(string[i])
    return count


def can_build_string(s1, s2, new_string, idx):
    if count_vowels(s1) == count_vowels(new_string) and ascii_sum(s1) == ascii_sum(new_string):
        print(new_string)
        return True
    if idx == len(s2):
        return False
    return can_build_string(s1, s2, new_string + s2[idx], idx + 1) or can_build_string(s1, s2, new_string, idx + 1)


def word(s1, s2):
    new_string = ""
    return can_build_string(s1, s2, new_string, 0)


s1 = "ula"
s2 = "wexcle"
print(word(s1, s2))