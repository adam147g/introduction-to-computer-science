"""
Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
class Node
..def init(self,val):
....self.val = val
....self.next = None
Zbiór mnogościowy liczb naturalnych reprezentowany jest przez listę o uporządkowanych rosnąco elementach.
Proszę napisać funkcję iloczyn(z1,z2,z3), która przekształca 3 listy (zbiory) z1,z2,z3 w jedną
listę (zbiór) zawierającą elementy będące częścią wspólna zbiorów z1,z2,z3. Funkcja powinna zwrócić
wskazanie do listy wynikowej.
Komentarz: Zadanie jest tak proste, że nie wymaga przykładu ani danych testowych.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def make_list(T):
    if len(T) == 0:
        return None
    tail = Node(T[-1])
    if len(T) == 1:
        return tail
    node = Node(T[-2])
    node.next = tail
    for i in range(len(T) - 3, -1, -1):
        nextnode = node
        node = Node(T[i])
        node.next = nextnode
    return node


def show(p):
    while p.next is not None:
        print(p.val, end=" -> ")
        p = p.next
    print(p.val)


def iloczyn(z1, z2, z3):
    def iloczyn2(p, q):
        p2 = Node(None)
        first = p2
        q2 = Node(None)
        p2.next = p
        q2.next = q
        while p is not None and q is not None:
            if p.val > q.val:
                q2.next = q.next
                q = q2.next
            elif p.val < q.val:
                p2.next = p.next
                p = p2.next
            else:
                p2 = p
                p = p.next
                q2 = q
                q = q.next
        return first.next

    return iloczyn2(iloczyn2(z1, z2), z3)


T_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
T_2 = [0, 3, 6, 9, 12, 15, 18, 21]
T_3 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

p = make_list(T_1)
q = make_list(T_2)
r = make_list(T_3)
show(p)
show(q)
show(r)
print()
show(iloczyn(p, q, r))
