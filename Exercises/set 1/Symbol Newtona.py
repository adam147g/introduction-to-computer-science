def newton(n, k):
    if n > k and n >= 0 and k >= 0:
        gora, dol1, dol2 = 1, 1, 1
        for i in range(1, n + 1):
            gora = i * gora
        for i in range(1, n - k + 1):
            dol1 = i * dol1
        for i in range(1, k + 1):
            dol2 = dol2 * i
        x = gora / (dol1 * dol2)
        return x
    elif k == 0 or k == n:
        return 1
    else:
        return False


n = int(input("n= "))
k = int(input("k= "))
print(newton(n, k))
