"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem A[n] = n * n + n + 1.
"""
number = int(input("Enter a number: "))
n = 1
A_n = 0
while number >= A_n:
    A_n = n * n + n + 1
    if number % A_n == 0:
        print("Number {0} is a multiple of A[{1}]".format(number,n))
        break
    else:
        n+=1
else:
    print("nie jest")