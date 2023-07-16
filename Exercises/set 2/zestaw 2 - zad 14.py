"""
Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą
wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
zadanych liczb.
"""
from math import sqrt
from time import perf_counter


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


a = perf_counter()
print(number_of_created_numbers(123, 71))
b = perf_counter()
print(b - a, "s")

'''
def create(num1, num2, bit_tab):
    str_num1 = str(num1)
    i = 0
    str_num2 = str(num2)
    j = 0
    new = ""
    for x in bit_tab:
        if x == 0:
            new += str_num1[i]
            i += 1
        else:
            new += str_num2[j]
            j += 1
    return int(new)


def add_and_check(bit_tab, zeros):
    if 0 not in bit_tab:
        return None
    i = len(bit_tab) - 1
    while i >= 0 and bit_tab[i] == 1:
        bit_tab[i] = 0
        i -= 1
    bit_tab[i] = 1
    check = 0
    for j in bit_tab:
        if j == 0:
            check += 1
    if check == zeros:
        return True
    return False

a=perf_counter()
count = 0
num1 = 123
num2 = 71
zeros = length(num1)
ones = length(num2)
bit_tab = [0] * (zeros + ones)
for i in range(ones):
    bit_tab[-i - 1] = 1

created = create(num1, num2, bit_tab)
if prime_number(created):
    count += 1
    print(created, bit_tab)
while True:
    flag = add_and_check(bit_tab, zeros)
    if flag is None:
        break
    if flag:
        created = create(num1, num2, bit_tab)
        if prime_number(created):
            count += 1
            print(created, bit_tab)
print(count)
b=perf_counter()
print(b-a)
'''
