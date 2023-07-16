"""
Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
kolejność jej elementów.
"""

from make_list_and_show import make_list, show

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def reverse_list(L):
    if L is None:
        return None
    p = None
    q = L.next
    while L is not None:
        L.next = p
        p = L
        L = q
        if q is not None:
            q = q.next
    return p

T_1 = [1, 2, 3, 10, 14, 18, 19]
p_1 = make_list(T_1)
show(p_1)
T_2 = [0, 4, 6, 11, 12, 13, 20]
p_2 = make_list(T_2)
show(p_2)
print()
p_1 = reverse_list(p_1)
show(p_1)
p_2 = reverse_list(p_2)
show(p_2)