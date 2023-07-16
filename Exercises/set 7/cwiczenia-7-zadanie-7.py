"""
Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji
należy przekazać wskazanie na pierwszy element listy.
"""
from make_list_and_show import show

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def remove_last_element(first):
    p = first
    q = p.next
    if p is None:
        return None
    r = q.next
    while r is not None:
        p = q
        q = r
        r = r.next
    q = None
    p.next = r
    return first

elem4 = Node(10)
elem3 = Node(5, elem4)
elem2 = Node(4, elem3)
elem1 = Node(1, elem2)
print(remove_last_element(elem1))
show(elem1)