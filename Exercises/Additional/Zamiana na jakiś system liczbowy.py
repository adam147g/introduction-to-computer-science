# Bit algo
# zamiana na jakiś system liczbowy

def print_in_k(n, k):
    if n == 0:
        return
    result = n % k
    print_in_k(n // k, k)
    if result > 9:
        result = chr(ord('A') + result - 10)
    print(result, end='')


n = int(input())
k = int(input())
print_in_k(n, k)
