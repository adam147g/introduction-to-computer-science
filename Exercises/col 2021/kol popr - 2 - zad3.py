"""
Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
class Node:
..def init (self,val,next=None):
....self.val = val
....self.next = next
Lista zawiera wartości będące liczbami naturalnymi Proszę napisać funkcję repair(p), (p wskazuje
na pierwszy element listy) która przekształca listę tak aby liczby parzyste znalazły się na końcu listy.
Funkcja powinna zwrócić wskazanie na przekształconą listę.
Komentarz: Można założyć, że lista wejściowa liczy więcej niż 2 elementy.
"""
from random import randint

# Adam Górka
class Node:
    def __init__(self, val, next=None):
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

'''
def repair(p):
    first = p
    lastodd = None
    q = first
    while (q != None):
        if (q.val % 2 == 1):
            lastodd = q
        q = q.next

    if (lastodd == None):
        return first

    while (first.val % 2 == 0):
        q = first
        first = first.next
        q.next = lastodd.next
        lastodd.next = q


    q = first.next
    p = first
    while (q != lastodd):
        if (q.val % 2 == 0):
            p.next = q.next
            q.next = lastodd.next
            lastodd.next = q
            q = p.next
        else:
            p = q
            q = q.next
    return first
'''

def repair(p):
    if p.val % 2 == 1:
        first = p
        while p.next is not None and p.next.val % 2 == 1:
            p = p.next
        tail = p.next
        f_tail = tail
        q = tail.next
    else:
        tail = p
        f_tail = tail
        while p.next is not None and p.next.val % 2 == 0:
            p = p.next
        first = p.next
        tail = p
        q = p.next

    while q is not None:
        if q.val % 2 == 0:
            tail.next = q
            tail = tail.next
            q = q.next
        else:
            p.next = q
            p = p.next
            q = q.next
    tail.next = None
    p.next = None
    p.next = f_tail

    return first





T = []
for i in range(10):
    T.append(randint(1,20))

print(T)
p = make_list(T)
show(p)
p = repair(p)
show(p)