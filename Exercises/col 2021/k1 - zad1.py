"""
Napis nazywamy wielokrotnym, jeżeli powstał przez n-krotne (n > 1) powtórzenie innego napisu o długości
co najmniej 1. Przykłady napisów wielokrotnych: ABCABCABC, AAAA, ABAABA. Dana jest tablica
T[N] zawierająca napisy. Proszę napisać funkcję multi(T), która zwraca długość najdłuższego napisu
wielokrotnego występującego w tablicy T lub wartość 0, jeżeli takiego napisu nie ma w tablicy.
"""
#zad1 Adam Górka

def test(string):
    n = len(string)
    for i in range(1, n//2 + 1):
        if n % i == 0:
            if string[:i] * (n//i) == string:
                return n
    return 0

def multi(T):
    n = len(T)
    max_dl = 0
    for i in range(n):
        max_dl = max(max_dl, test(T[i]))
    return max_dl

T = ['ABCABCABC','AAAA','ABAABA']
print(multi(T))