number = int(input("Podaj liczbę naturalną: "))
starting_number = 1
i = 0
result = 1
while result <= number:
    starting_number += 2
    result += starting_number
    i += 1
print("Pierwiastek tej liczby wynosi:", i)
