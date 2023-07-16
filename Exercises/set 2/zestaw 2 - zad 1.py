"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.
"""

number = int(input("Enter a number: "))
factors=[]

for i in range(1,number+1):
    if number % i == 0:
        factors.append(i)

def is_in_fibo(number,a,b):
    while number > a+b:
        a=a+b
        b=a+b
    if number==b or number==a or number==a+b:
        return True
    return False

flag=False

for i in factors:
    if is_in_fibo(i,a=0,b=1) and is_in_fibo(int(number/i),a=0,b=1):
        flag=True
        break
if flag:
    print("jest")
else:
    print("nie jest")



'''
def is_product_of_Fib(number, a, b):
    while number > a * b:
        a = a + b
        b = a + b
    if number == a * b:
        return True
    return False



#print(is_product_of_Fib(number, a=1, b=1))
'''