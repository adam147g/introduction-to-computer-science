"""
Dana jest N-elementowa tablica t zawierająca liczby naturalne mniejsze od 1000. Proszę napisać
funkcję, która zwraca długość najdłuższego, spójnego fragmentu tablicy, dla którego w iloczynie
jego elementów każdy czynniki pierwszy występuje co najwyżej raz. Na przykład dla tablicy
t=[2,23,33,35,7,4,6,7,5,11,13,22] wynikiem jest wartość 5.
"""
from math import sqrt, ceil

'''
def prime_factor_occurs_once(number):
    if number % 4 == 0:
        return False
    for i in range(3, ceil(sqrt(number)) + 1):
        if number % i == 0:
            number //= i
        if number % i == 0:
            return False
    return True


def longest_sequence(T):
    max_length = 0
    for i in range(len(T)):
        actual_length = 0
        j = i + 1
        product = T[i]
        while j < len(T) and prime_factor_occurs_once(product):
            product *= T[j]
            j += 1
            actual_length += 1
        max_length = max(max_length, actual_length)
    return max_length
'''


def fact(num, factors):
    if num == 1:
        return factors
    flg = True
    i = 2
    while i <= num:
        count = 0
        while num % i == 0 and count < 2:
            num //= i
            count += 1
        if count > 0:
            factors.append(i)
        if count > 1:
            flg = False
            break
        i += 1
    if flg:
        return factors
    return None


def zad20(T):
    max_length = 0
    for i in range(len(T)):
        actual_length = 0
        factors = []
        factors=fact(T[i],factors)
        j=i+1
        out=False
        if factors is not None:
            actual_length+=1
            while j<len(T):
                new_factors = []
                new_factors=fact(T[j],new_factors)
                if new_factors is not None:
                    for x in new_factors:
                        if x not in factors:
                            factors.append(x)
                        else:
                            out=True
                            break
                else:
                    out=True
                if out:
                    break
                j+=1
                actual_length+=1
        max_length=max(actual_length,max_length)
    return max_length

T = [2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 22]
print(zad20(T))
