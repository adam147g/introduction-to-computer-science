a = 1
b = 1
print(a, end=", ")
print(b, end=", ")
while a < 1000000:
    a = a + b
    print(a, end=", ")
    b = a + b
    print(b, end=", ")
print()
print("---------------")
a = 1
b = 1
print(1, end=", ")
while a < 1000000:
    b = a + b
    a = b - a
    print(a, end=", ")
print(b)
