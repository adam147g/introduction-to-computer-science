"""
Dana jest liczba naturalna o niepowtarzających się cyfrach pośród których nie ma zera. Ile różnych
liczb podzielnych np. przez 7 można otrzymać poprzez wykreślenie dowolnych cyfr w tej liczbie.
Np. dla 2315 będą to 21, 35, 231, 315.

->DYGRESJA DO MASKI BITOWEJ<-
Zadanie: w słowie ośmiobitowym wyzerować 2 najmłodsze bity.

Rozwiązanie: należy użyć operatora AND (iloczyn) i maski bitowej 11111100.

słowo: 10010111
maska: 11111100
wynik: 10010100

3 = 10     - w naszym zadaniu zwracana będzie przedostatnia cyfra
10 = 01010 -     ----------- | | -----------  4 i 2 cyfra od końca - print(bit_mask(2315,10)) -> 21

"""


def length(number):
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count


def bit_mask(number, mask):
    actual_number = 0
    while number > 0:
        if mask % 2 == 1:
            actual_number *= 10
            actual_number += number % 10
        number //= 10
        mask //= 2
    new_number = 0
    while actual_number > 0:
        new_number *= 10
        new_number += actual_number % 10
        actual_number //= 10
    return new_number


def number_without_zero(number):
    count = 0
    number_length = length(number)
    for i in range(1, 2 ** number_length):
        if bit_mask(number, i) % 7 == 0:
            count += 1
    return count


print(number_without_zero(2315))
print()
print(bit_mask(2315,3))
print(bit_mask(2315,10))