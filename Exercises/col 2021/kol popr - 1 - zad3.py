"""
Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
class Node:
..def init(self,val,next=None):
....self.val = val
....self.next = next
Lista zawierała wartości stanowiące kolejne wyrazy ciągu arytmetycznego. Z wnętrza listy usunięto
pewną liczbę elementów. Proszę napisać funkcję repair(p), (p wskazuje na pierwszy element listy) która
uzupełnia listę elementami, tak aby ponownie zawierała kolejne wyrazy ciągu arytmetycznego. Funkcja
powinna zwrócić liczbę wstawionych elementów.
Komentarz: Można założyć, że lista wejściowa liczy więcej niż 2 elementy.
"""
from random import randint

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


def make_list(T):
    if len(T) == 0:
        return None
    tail = Node(T[-1])
    if len(T) == 1:
        return tail
    node = Node(T[-2], tail)
    for i in range(len(T) - 3, -1, -1):
        nextnode = node
        node = Node(T[i], nextnode)
    return node


def show(p):
    while p.next is not None:
        print(p.val, end=" -> ")
        p = p.next
    print(p.val)


def szukaj(p):
    res = -(p.val-p.next.val)
    p = p.next
    while p.next != None:
        t = -(p.val-p.next.val)
        if t < 0:
            res = max(t,res)
        else:
            res = min(t,res)
        p = p.next
    return res

def repair(p):
    first = p
    r = szukaj(p)
    count = 0
    while p.next is not None:
        if p.val + r != p.next.val:
            node = Node(p.val + r, p.next)
            p.next = node
            count += 1
        p = p.next

    return first, count


r = 2048
T = []
i = -2
while i < 10000:
    T.append(i * r)
    i += 1
p = make_list(T)
show(p)

for i in range(4563):
    T.remove(T[randint(1, len(T) - 2)])

p = make_list(T)
show(p)

p, count = repair(p)
print()
show(p)
print()
print(count)