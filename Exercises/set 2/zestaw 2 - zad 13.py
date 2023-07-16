"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie,
czy liczba zakończona jest unikalną cyfrą.
"""


def unique_number_check(number):
    '''
    strnumber = str(number)
    lastnumber = number % 10
    for i in range(len(strnumber) - 1):
        if strnumber[i] != str(lastnumber):
            continue
        else:
            return False
    return True
    '''

    potential_unique = number % 10
    number//=10
    while number>0:
        if number%10==potential_unique:
            return False
        number//=10
    return True


number = int(input(">> "))
print(unique_number_check(number))
