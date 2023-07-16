"""
Napisać program wyznaczający wartość do której zmierza iloraz dwóch kolejnych wyrazów
ciągu Fibonacciego. Wyznaczyć ten iloraz dla różnych wartości początkowych wyrazów ciągu.
"""


def Fibonacci(a, b):
    while a < 1000:
        a = a + b
        b = a + b
    return a / b


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
result = Fibonacci(number1, number2)
print("The quotient of the two consecutive numbers of the sequence tends to", result)