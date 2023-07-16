"""
Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
element listy o wartościach typu int, usuwającą wszystkie elementy, których
wartość dzieli bez reszty wartość bezpośrednio następujących po nich
elementów.
"""

from make_list_and_show import make_list, show

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def remove_divisible_numbers(first):
    p = first
    q = p.next
    if p is None:
        return None
    while q is not None and q.next is not None:
        if q.value % p.value == 0:
            p = p.next
            q = p.next
        else:
            p.next = q.next
            p = p.next
            q = p.next
    if q is not None and q.value % p.value != 0:
        p.next = None
        p = p.next
    elif q is not None and q.value % p.value == 0:
        p = p.next
        q = p.next

T = [1, 2, 3, 3, 2, 63, 3, 53, 4, 2, 1, -1, -3]
p = make_list(T)
show(p)
remove_divisible_numbers(p)
show(p)