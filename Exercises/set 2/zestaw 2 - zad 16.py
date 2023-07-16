"""
Liczba Smitha to taka, której suma cyfr jest równa sumie cyfr wszystkich liczb występujących
w jej rozkładzie na czynniki pierwsze. Na przykład: 85 = 5∗17, 8+5 = 5+1+7. Napisać program
wypisujący liczby Smitha mniejsze od 1000000.



!!! TREŚĆ NIE WYDAJE SIĘ TRUDNA, ALE NIE CHCE MI SIĘ ANALIZOWAĆ KODU!!!

"""
from math import sqrt


def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        while i <= sqrt(n):
            if n % i == 0:
                return False
            i += 2
            if n % i == 0:
                return False
            i += 4
        return True


def digits_summary(number):
    summary = 0
    while number != 0:
        summary += number % 10
        number //= 10
    return summary


def prime_factor(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def lower_number(number):
    i = 2
    numbers = []
    summary = 0
    while number > 1:
        if number % i == 0:
            number //= i
            numbers.append(i)
        else:
            i += 1
    for num in numbers:
        if is_prime(num):
            summary += num
    return summary


def smith_number(number):
    while number > 0:
        copy_number = number
        num_digits = digits_summary(number)
        for i in range(2, number):
            if copy_number % i == 0:
                copy_number //= i
                factor = i
                if not is_prime(copy_number) and prime_factor(factor):
                    lowered_cp_num = lower_number(copy_number)
                    fac_num_digits = digits_summary(factor)
                    num_digits2 = lowered_cp_num + fac_num_digits
                    if num_digits == num_digits2:
                        print(number,end=" ")
                        break
                elif prime_factor(copy_number) and prime_factor(factor):
                    fac_num_digits = digits_summary(factor)
                    cp_num_digits = digits_summary(copy_number)
                    num_digits2 = cp_num_digits + fac_num_digits
                    if num_digits == num_digits2:
                        print(number,end=" ")
                        break
                copy_number = number
        number -= 1


smith_number(60)