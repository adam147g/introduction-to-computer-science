"""
Dana jest liczba naturalna N. Proszę zaimplementować funkcję divide(N), która sprawdza czy jest możliwe
pocięcie liczby N na kawałki, tak aby każdy z kawałków był liczba pierwszą oraz liczba kawałków też była
liczbą pierwszą. Funkcja powinna zwracać wartość logiczną. Na przykład: divide(2347)=True, podział na
23 i 47, natomiast divide(2255)=False.
Przykładowe wywołania funkcji:
print(divide(273)) # True, podział 2|7|3
print(divide(22222)) # True, podział 2|2|2|2|2
print(divide(23672)) # True, podział 23|67|2
print(divide(2222)) # False
print(divide(21722)) # False
"""

def isprime(n):
    if n == 0 or n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def divide(n, c = 1):   # c - liczba części. n to część, którą sprawdzamy
    if isprime(n) and isprime(c):
        return True
    else:               # odcinamy liczbę pierwszą na końcu i sprawdzamy resztę rekurencyjnie
        p = 10
        x = n % p
        while x < n:
            x = n % p
            if isprime(x):
                if divide(n // p, c + 1):
                    return True
            p *=10
    return False


print(divide(273))      # True, podział 2|7|3
print(divide(22222))    # True, podział 2|2|2|2|2
print(divide(23672))    # True, podział 23|67|2
print(divide(2222))     # False
print(divide(21722))    # False
print(divide(2737))     # True, podział 2|73|7
print(divide(1111111111))   # True, podział 11|11|11|11|11
print(divide(111111112))    # True, podział 11|11|11|11|2
print(divide(111111111111)) # False
print(divide(2255))     # False