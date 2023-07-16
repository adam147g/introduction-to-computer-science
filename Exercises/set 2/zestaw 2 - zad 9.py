"""
Napisać program, który oblicza pole figury pod wykresem funkcji y = 1/x w przedziale
od 1 do k, metodą prostokątów.
"""

b = int(input("Enter a range: "))
n = int(input("How many rectangles do you want to split the diagram into: "))
a = 1
if b < a:
    print("ERROR")
    exit(0)
elif b == a:
    print("Pole = 0")
    exit(0)

x = (b - a) / n     # bok prostkąta + tyle będziemy dodawać
center = a + x / 2  # środek prostokąta
y = 1 / center      # wysokość prostokąta
summary = 0         # pole łączne

while a + x <= b:
    summary += x * y
    a += x
    center += x
    y = 1 / center

print(summary)
