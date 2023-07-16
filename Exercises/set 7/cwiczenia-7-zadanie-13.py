"""
Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
element listy o wartościach typu int, usuwającą wszystkie elementy, których
wartość jest mniejsza od wartości bezpośrednio poprzedzających je
elementów.
"""

from make_list_and_show import make_list, show

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def remove_lesser_number(first):
    p = first
    q = p.next
    if p is None:
        return None
    while q is not None and q.next is not None:
        if p.value <= q.value:
            p = p.next
            q = p.next
        else:
            p.next = q.next
            p = p.next
            q = p.next
    if q is not None and p.value > q.value:
        p.next = None
        p = p.next
    elif q is not None and p.value <= q.value:
        p = p.next
        q = p.next

T = [1, 2, 3, 3, 2, 63, 1, 53, 4, 3, 0, -1, -3]
p = make_list(T)
show(p)
remove_lesser_number(p)
show(p)