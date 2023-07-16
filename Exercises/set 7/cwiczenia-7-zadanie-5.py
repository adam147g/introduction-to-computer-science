"""
Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do
10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy
należy połączyć w jedną listę odsyłaczową, która jest posortowana
niemalejąco według ostatniej cyfry pola val.
"""

from make_list_and_show import make_list, show
from random import randint

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def split(head):
    if head is None:
        return None
    first = [None]*10
    last = [None]*10
    while head is not None:
        c = head.value % 10
        if first[c] is None:
            first[c] = last[c] = head
        else:
            last[c].next = head
            last[c] = last[c].next
        head = head.next

    i = 0
    remember = None
    while i < 10:
        if first[i] is not None and remember is None:
            f = first[i]
            remember = i
        elif first[i] is not None:
            last[remember].next = first[i]
            remember = i
        i += 1
    last[remember].next = None
    return f

T_1 = [randint(0,100) for _ in range(10)]
T_2 = [randint(0,100) for _ in range(10)]
p_1 = make_list(T_1)
p_2 = make_list(T_2)
show(p_1)
show(p_2)
print()
p_1 = split(p_1)
p_2 = split(p_2)
show(p_1)
show(p_2)
