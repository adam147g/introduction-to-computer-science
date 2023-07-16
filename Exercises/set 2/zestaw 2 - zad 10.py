"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie,
czy liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem A[n] = 3 ∗ A[n−1] + 1,
a pierwszy wyraz jest równy 2.
"""
number = int(input(">> "))
an = 2
if number % an == 0:
    print("YES")
    exit(0)
while number >= an:
    an = (3 * an) + 1
    if number % an == 0:
        print("YES")
        break
else:
    print("NO")
