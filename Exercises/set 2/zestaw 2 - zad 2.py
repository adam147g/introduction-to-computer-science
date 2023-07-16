"""
Napisać program wczytujący trzy liczby naturalne a,b,n i wypisujący rozwinięcie dziesiętne
ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej (n jest rzędu 100).
"""

# 1ST SOLUTION
"""
a = int(input("Enter a numerator: "))
b = int(input("Enter a denominator: "))
n = int(input("Enter a number: "))
number = a/b
str_number = str(number)
print(str_number[0:n+2], sep="")
"""

# 2ND SOLUTION
a = int(input("Enter a numerator: "))
b = int(input("Enter a denominator: "))
n = int(input("Enter a number: "))
c = a // b
print(c, ".", sep="", end="")
r = 10 * (a % b)
for i in range(n):
    r = 10 * r
    print(r // b, end="")
    r %= b
print()
