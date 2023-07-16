"""
Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż 2, 3, 5.
Jedynka też jest taką liczbą. Napisz program, który wylicza ile takich liczb znajduje się w przedziale
od 1 do N włącznie.
"""

starting_number = int(input("Podaj N: "))
n = starting_number
i = 1

while n > 0:
    if n == 1:
        print(n,end=" ")
        break
    else:
        while n % 2 == 0:
            n = n / 2
            if n == 1:
                print(starting_number,end=" ")
                i+=1
        else:
            while n % 3 == 0:
                n = n / 3
                if n == 1:
                    print(starting_number,end=" ")
                    i+=1
            else:
                while n % 5 == 0:
                    n = n / 5
                    if n == 1:
                        print(starting_number,end=" ")
                        i+=1
                else:
                    starting_number -= 1
                    n=starting_number
print()
print(i)
