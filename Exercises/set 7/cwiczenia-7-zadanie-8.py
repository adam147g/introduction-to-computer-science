"""
Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
element listy. Do funkcji należy przekazać wskazanie na pierwszy element
listy
"""

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def remove_every_other(first):
    p = first
    if p is None:
        return None
    while p.next is not None and p.next.next is not None:
        p.next = p.next.next
        p = p.next
    if p.next is not None:
        p.next = None
    return p.value


def printinf(first):
    p = first
    if p is None:
        print("Pusta")
    else:
        q = p.next
        while(q.next is not None):
            print(p.value, end = " -> ")
            p = q
            q = q.next
        print(p.value, "->", q.value)



elem5 = Node(11)
elem4 = Node(9, elem5)
elem3 = Node(5, elem4)
elem2 = Node(4, elem3)
elem1 = Node(1, elem2)

printinf(elem1)
print(remove_every_other(elem1))
printinf(elem1)