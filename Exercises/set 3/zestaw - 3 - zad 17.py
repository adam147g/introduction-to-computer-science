"""
Dane są dwie N-elementowe tablice t1 i t2 zawierające liczby naturalne. Z wartości w obu tablicach
możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element (z tablicy
t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8] poprawnymi
sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8. Proszę napisać funkcje generującą
i wypisująca wszystkie poprawne sumy, które są liczbami pierwszymi. Do funkcji należy przekazać dwie
tablice, funkcja powinna zwrócić liczbę znalezionych i wypisanych sum.
"""
# zapisywanie liczb w systemie trójkowym i kiedy 0 - dodawanie z t1, 1 - dodawanie z t2, 2 - dodawanie t1 + t2

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


def convert_decimal_number(number, length):
    array = [0] * length
    for i in range(length - 1, -1, -1):
        array[i] = number % 3
        number //= 3
    return array


def create_sum(T1, T2, idx):
    summary = 0
    result = convert_decimal_number(idx, len(T1))
    for i in range(len(result)):
        if result[i] == 0:
            summary += T1[i]
        elif result[i] == 1:
            summary += T2[i]
        elif result[i] == 2:
            summary += (T1[i] + T2[i])
    return summary


def correct_sum(T1, T2):
    count = 0
    for i in range(3 ** len(T1)):
        summary = create_sum(T1, T2, i)
        if prime_number(summary):
            print(summary)
            count += 1
    print()
    return count

T1 = [1, 3, 2, 4]
T2 = [9, 7, 4, 8]
print(correct_sum(T1, T2))