number = 1
result1 = 0
result2 = 0
while number < 1000000:
    for i in range(1, number):
        if number % i == 0:
            result1 += i
    dzielnikiResult1 = result1

    for j in range(1, dzielnikiResult1):
        if dzielnikiResult1 % j == 0:
            result2 += j
    dzielnikiResult2 = result2

    if number == dzielnikiResult2 and number != dzielnikiResult1:
        print("Liczby", number, "i", dzielnikiResult1, "są liczbami zaprzyjaźnionymi.")
    result1 = 0
    result2 = 0
    number += 1
