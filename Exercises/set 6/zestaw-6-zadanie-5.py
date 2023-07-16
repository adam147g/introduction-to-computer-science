from math import sqrt


def number_converter(number):
    str_number = str(number)
    digits = list()
    for i in range(len(str_number)):
        digits += str_number[i]
    return digits


def is_prime_number(number):
    if number == 2 or number == 3:
        return True
    elif number < 2 or number % 2 == 0 or number % 3 == 0:
        return False
    else:
        i = 5
        while i <= sqrt(number):
            if number % i == 0:
                return False
            i += 2
            if number % i == 0:
                return False
            i += 4
        return True


def convert_to_decimal(binary_number):
    decimal_number = 0
    i = 0
    while binary_number != 0:
        decimal = binary_number % 10
        decimal_number += decimal*pow(2, i)
        binary_number //= 10
        i += 1
    return decimal_number


def binary_sequence(array, p=0, max_length=0, binary_number=''):
    if p == len(array) and max_length < 30:
        exit("True")
    for i in range(p, len(array)):
        binary_number += str(array[i])
        int_binary_number = int(binary_number)
        decimal = convert_to_decimal(int_binary_number)
        if is_prime_number(decimal):
            length = len(binary_number)
            if length > max_length:
                max_length = length
            binary_sequence(array, i+1, max_length)
    return False

number = 111011
array = number_converter(number)
print(binary_sequence(array))

'''
number = 110100
array = number_converter(number)
print(binary_sequence(array))
'''