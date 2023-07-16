"""
Napisać program znajdujący wszystkie liczby N-cyfrowe dla których suma N-tych potęg cyfr
liczby jest równa tej liczbie, np. 153 = 1**3 + 5**3 + 3**3 .
"""


def mathematical_power(number):
    up=10**number
    dwn=(10**(number-1))-1
    while up > dwn:
        a = up
        power = 1
        up_check = 0
        i = 0
        strup = str(up)
        while strup[i:-1:1]:
            power += 1
            i += 1
        x = power
        while a > 0:
            c = a % 10
            a = a // 10
            up_check += c ** x
        if up_check == up:
            print(up,end=" ")
        up -= 1


number = int(input(">> "))
mathematical_power(number)