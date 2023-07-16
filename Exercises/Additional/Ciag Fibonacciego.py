# Bit algo
# Ciąg Fibonacciego
def fib(n, a):
    if a[n] != -1:
        return a[n]  # zapamiętywanie obliczonych  już wyrazów ciągu

    if n < 1:
        return 1

    a[n] = fib(n - 1, a) + fib(n - 2, a)
    return a[n]


a = [-1 for _ in range(101)]

print(fib(1, a))
