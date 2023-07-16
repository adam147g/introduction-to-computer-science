def NWD(number1, number2):
    while number2 != 0:
        c = number1 % number2
        number1 = number2
        number2 = c
    return number1


def NWW(number1, number2):
    return (number1 * number2 / NWD(number1, number2))


number1 = int(input("Podaj pierwszą liczbę: "))
number2 = int(input("Podaj drugą liczbę: "))
number3 = int(input("Podaj trzecią liczbę: "))

print("NWW tych 3 liczb to: " + str(NWW(NWW(number1, number2), number3)))
