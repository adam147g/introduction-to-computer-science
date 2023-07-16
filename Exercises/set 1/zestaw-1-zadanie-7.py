"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.
"""
number = int(input("Enter a number: "))
a = 1
b = 1
flag = True
if number == 1:
    print("Number", 1, "is product of", 1, "and", 1, "which belong to the Fibonacci sequence.")
    flag = False

while a < 1000 and flag:
    a = a + b
    if (a * b) == number:
        print("Number", number, "is product of", a, "and", b, "which belong to the Fibonacci sequence.")
        flag = False
        break
    b = a + b
    if (a * b) == number:
        print("Number", number, "is product of", a, "and",
              b, "which belong to the Fibonacci sequence.")
        flag = False
        break

if flag:
    print("Number is not a product of any two numbers which belong to the Fibonacci sequence.")
