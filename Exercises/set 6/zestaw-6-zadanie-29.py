"""
Punkt leżący w przestrzeni jest opisywany trójką liczb typu float (x,y,z). Tablica T[N] zawiera
współrzędne N punktów leżących w przestrzeni. Punkty posiadają jednostkową masę. Proszę napisać funkcję,
która sprawdza czy istnieje podzbiór punktów liczący co najmniej 3 punkty, którego środek ciężkości leży w
odległości nie większej niż r od początku układu współrzędnych. Do funkcji należy przekazać tablicę T oraz
promień r, funkcja powinna zwrócić wartość typu bool.

"""
from random import random


def distance(res,r):
    x=y=z=0
    for point in (res):
        x+=point[0]
        y+=point[1]
        z+=point[2]
    x/=len(res)
    y/=len(res)
    z/=len(res)
    if (x**2+y**2+z**2)**(1/2)<=r:
        return True
    return False



def zad29(T,r,idx=0,res=[]):

    if len(res)>2:
        dist=distance(res,r)
        if dist:
            print(res)
            return True
        return False
    if idx < len(T):
        res.append(T[idx])
        if zad29(T,r,idx+1,res):
            return True
        res.remove(T[idx])
        if zad29(T,r,idx+1,res):
            return True
    return False

t=[]
for i in range(20):
    t.append((random()*10,random()*10,random()*10))


print()
print(zad29(t,1.99))
print()
print(zad29(t,2.3))
print()
print(zad29(t,3))
print()
print(zad29(t,5.2))
print()
print(zad29(t,7.3))