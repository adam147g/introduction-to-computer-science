
n = int(input("Podaj n: "))
k = int(input("Podaj k: "))
summary_n = 1
summary_k = 1
summary_minus = 1
minus = n - k
if n > k:
    for number in range(1, n+1):
        summary_n *= number
    for number in range(1, k+1):
        summary_k *= number
    for number in range(1, minus+1):
        summary_minus *= number
result = summary_n / (summary_k * summary_minus)
print(result)
if n < k:
    print("N musi być większe od k!")



# 2ND SOLUTION
epsilon = 0.0000000001


def element(P):
    a = 1
    b = P
    while abs(a - b) >= epsilon:
        a = (a + b) / 2
        b = P / a
    return a


number = int(input("Enter a number: "))
element_result = element(number)
print(element_result)
