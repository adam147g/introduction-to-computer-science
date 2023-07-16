"""
Napisać program wyliczający pierwiastek równania x**x = 2020 metodą stycznych.
"""
import math

number = 2020
x = 5
epsilon = 0.0001
e = float(math.e)

while x ** x - 2020 > epsilon:
    function = x ** x
    lnx = x * math.log(1 + x)
    derivative = e ** lnx
    x = x - function / derivative
    if x ** x - 2020 < 0:
        x += 1

print(x,x**x)