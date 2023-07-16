"""
Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do
funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą
wartość.
"""
from make_list_and_show import show

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def add_last_element(first, value):
    p = first
    q = p.next
    if p is None:
        return None
    while q is not None:
        p = q
        q = p.next
    q = Node(value)
    p.next = q
    return first



elem3 = Node(5)
elem2 = Node(4, elem3)
elem1 = Node(1, elem2)
print(add_last_element(elem1, 23))
show(add_last_element(elem1,123))