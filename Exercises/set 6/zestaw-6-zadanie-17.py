"""
Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą
wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
zadanych liczb.
"""
from math import sqrt


def prime_number(a):
    if a == 2 or a == 3:
        return True
    elif a < 2 or a % 2 == 0 or a % 3 == 0:
        return False
    else:
        i = 5
        while i <= sqrt(a):
            if a % i == 0:
                return False
            i += 2
            if a % i == 0:
                return False
            i += 4
        return True


def length(number):
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count


def number_of_created_numbers(num_1, num_2, rest=0):
    count = 0
    if num_1 == 0 and num_2 == 0 and prime_number(rest):
        count += 1
    if num_1 > 0:
        num_1_pow = 10 ** (length(num_1) - 1)
        count += number_of_created_numbers(num_1 % num_1_pow, num_2, rest * 10 + num_1 // num_1_pow)
    if num_2 > 0:
        num_2_pow = 10 ** (length(num_2) - 1)
        count += number_of_created_numbers(num_1, num_2 % num_2_pow, rest * 10 + num_2 // num_2_pow)
    return count


print(number_of_created_numbers(123, 71))