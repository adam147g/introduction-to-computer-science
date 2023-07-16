"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie,
czy jej cyfry stanowią ciąg rosnący.
"""


def are_digits_incresing_string(strnumber, i=1):
    while i != len(strnumber):
        if strnumber[i] > strnumber[i - 1]:
            i += 1
        else:
            return False
    return True


def are_digits_incresing_int(number):
    while number > 10:
        if number % 10 > (number % 100) // 10:
            number //= 10
        else:
            return False
    return True


number = int(input("Enter a number: "))
str_number = str(number)
print(are_digits_incresing_string(str_number))
print(are_digits_incresing_int(number))
