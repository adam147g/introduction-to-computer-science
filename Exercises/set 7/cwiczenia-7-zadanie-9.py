"""
Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne
elementy listy przechowują kolejne cyfry. Proszę napisać funkcję
zwiększającą taką liczbę o 1
"""

class Node:
    def __init__(self, value=None, prev=None, next_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev


def increase_by_one(first):
    p = first
    increase = False
    while p.next is not None:
        p = p.next
    while p is not None:
        if p.value < 9 and not increase:
            p.value += 1
            increase = True
        if p.value == 9 and not increase:
            p.value = 0
            increase = False
        print(p.value, end="")
        p = p.prev
    if p is None and not increase:
        p = Node(1, None, p)
        print(p.value)


elem1 = Node(7)
elem2 = Node(4, elem1)
elem1.next = elem2
elem3 = Node(9, elem2)
elem2.next = elem3
increase_by_one(elem1)