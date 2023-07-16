"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie,
czy liczba ta zawiera cyfrę równą liczbie swoich cyfr.
"""
number = int(input(">> "))
strnumber = str(number)
i = 0
tab=[0]*10

while i != len(strnumber):
    tab[int(strnumber[i])]+=1
    i += 1
result=0
for i in range(len(tab)):
    if tab[i]!=0:
        result+=1

j = 0
while j<len(strnumber):
    if int(strnumber[j]) == result:
        print("ya")
        break
    else:
        j += 1
else:
    print("nope")