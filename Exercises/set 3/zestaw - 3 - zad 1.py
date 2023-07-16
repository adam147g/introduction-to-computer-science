"""
MOJE ROZWIĄZANIE
def binary_system(number):
    binaryList = list()
    while number != 0:
        remainder = number % 2
        number = number // 2
        binaryList.append(remainder)
    binaryList.reverse()
    return binaryList


def octal_system(number):
    numberList = list()
    octallist = list()
    strnumber = str(number)
    i = 0
    result = 0
    power = 0
    for i in strnumber:
        numberList.append(i)
        power += 1
    power = power - 1
    for x in numberList:
        y = int(x)
        decimalNumber = y * (8 ** power)
        power -= 1
        result += decimalNumber
    octallist.append(result)
    return octallist


def hexadecimal_system(number):
    hexadecimalList = list()
    while number != 0:
        remainder = number % 16
        number = number // 16
        hexadecimalList.append(remainder)
    return hexadecimalList


number = int(input("Podaj liczbę: "))
choice = input(
    "Podaj wybór 1 (dwójkowy) lub 2 (ósemkowy) lub 3 (szesnastkowy): ")
if choice == "1":
    print(binary_system(number))
elif choice == "2":
    print(octal_system(number))
elif choice == "3":
    print(hexadecimal_system(number))

# ROZWIĄZANIE NA ĆWICZENIACH
from math import log
from math import ceil


def number_base_change(number, base):
    hex = "0123456789ABCDEF"
    resultList = [0 for _ in range(ceil(log(number, base)))]
    i = 0
    while number > 0:
        resultList[i] = number % base
        number //= base
        i += 1
    resultList.reverse()
    for j in resultList:
        print(hex[j], end="")


number_base_change(255, 16)
"""


def baseconvert(number, base):
    if number==0:
        return "0"
    a = ""
    hex = "0123456789ABCDEF"
    while number > 0:
        a = hex[number % base] + a  # jest różnica między a = hex[number % base] + a
                                    #                     a = a + hex[number % base]
        number = number // base
    return a

print(baseconvert(250, 16))