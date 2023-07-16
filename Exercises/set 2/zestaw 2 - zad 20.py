"""
Dwie liczby naturalne są różno-cyfrowe jeżeli nie posiadają żadnej wspólnej cyfry. Proszę napisać
program, który wczytuje dwie liczby naturalne i poszukuje najmniejszej podstawy systemu (w zakresie
2-16) w którym liczby są różno-cyfrowe. Program powinien wypisać znalezioną podstawę, jeżeli podstawa
taka nie istnieje należy wypisać komunikat o jej braku. Na przykład: dla liczb 123 i 522 odpowiedzią jest
podstawa 11 bo 123(10) = 102(11) i 522(10) = 435(11) .
"""


def number_base_converter(number, base):
    if number == 0:
        return "0"
    a = ""
    hex = "0123456789ABCDEF"
    while number > 0:
        a = hex[number % base] + a
        number = number // base
    return a


def different_digits(number_1, number_2):
    while True:
        for i in range(2, 17):
            count = 0
            change_1 = number_base_converter(number_1, i)
            print(number_1, " - ", change_1, "\t({0})".format(i))
            change_2 = number_base_converter(number_2, i)
            print(number_2, " - ", change_2, "\t({0})".format(i))
            print("----------")
            for j in range(len(change_1)):
                if change_1[j] not in change_2:
                    count += 1
                if count == len(change_1):
                    return i
        return False


print(different_digits(9, 0))
print()
print(different_digits(123, 522))
