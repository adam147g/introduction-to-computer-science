"""
Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do
której przekazujemy wskaźnik na początek oraz wartość klucza. Jeżeli
element o takim kluczu występuje w liście należy go usunąć z listy. Jeżeli
elementu o zadanym kluczu brak w liście należy element o takim kluczu
wstawić do listy.
"""
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def remove_key(first, key):
    p = first
    q = p.next
    temp = False
    if p is None:
        return None
    if first.value == key:
        p = None
        return p
    while q is not None and q.value is not key and not temp:
        p = q
        q = p.next
    if q is not None and q.value == key:
        p.next = q.next
    else:
        q = Node(key)
        p = q
        q = p.next
    return p.value

elem4 = Node(5)
elem3 = Node(55, elem4)
elem2 = Node(4, elem3)
elem1 = Node(1, elem2)
print(remove_key(elem1, 4))
print((remove_key(elem1,20)))