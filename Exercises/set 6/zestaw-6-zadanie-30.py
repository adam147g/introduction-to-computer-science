"""
Punkt leżący na płaszczyźnie jest opisywany parą liczb typu float (x,y). Tablica T[N] zawiera
współrzędne N punktów leżących na płaszczyźnie. Punkty posiadają jednostkową masę.
Proszę napisać funkcję, która sprawdza czy istnieje niepusty podzbiór n punktów, gdzie n|k oraz n jest
wielokrotnością liczby 3, którego środek ciężkości leży w odległości mniejszej niż r od początku
układu współrzędnych. Do funkcji należy przekazać dokładnie 3 parametry: tablicę t, promień r,
oraz ograniczenie k, funkcja powinna zwrócić wartość typu bool.
"""
from random import random


def distance(res,r):
    x=y=0
    for point in (res):
        x+=point[0]
        y+=point[1]
    x/=len(res)
    y/=len(res)
    if (x**2+y**2)**(1/2)<r:
        return True
    return False



def zad30(T,r,k,idx=0,res=[]):
    n=len(res)
    if n > 0 and n%k==0 and n%3==0:
        dist = distance(res, r)
        if dist:
            print(res)
            return True
        return False
    if idx < len(T):
        res.append(T[idx])
        if zad30(T, r, k, idx + 1, res):
            return True
        res.remove(T[idx])
        if zad30(T, r, k, idx + 1, res):
            return True
    return False



k=2
t=[]
for i in range(20):
    t.append((random()*10,random()*10))


print()
print(zad30(t,1.99,k))
print()
print(zad30(t,2.3,k))
print()
print(zad30(t,3,k))
print()
print(zad30(t,5.2,k))
print()
print(zad30(t,7.3,k))