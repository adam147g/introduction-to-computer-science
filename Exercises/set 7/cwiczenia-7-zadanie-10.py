"""
Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać
funkcję dodającą dwie takie liczby. W wyniku dodawania dwóch liczb powinna
powstać nowa lista
"""

class Node:
    def __init__(self, value=None, prev=None, next_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev


def add_two_numbers(first1, first2):
    p = first1
    q = first2
    remainder = False
    while p.next is not None and q.next is not None:
        p = p.next
        q = q.next
    while p is not None and q is not None:
        if p.value + q.value > 9:
            if remainder:
                number = (p.value + q.value + 1) % 10
            else:
                number = (p.value + q.value) % 10
            remainder = True
            print(number)
        elif p.value + q.value < 10 and remainder:
            if p.value + q.value + 1 == 10:
                number = (p.value + q.value + 1) % 10
                print(number)
                remainder = True
            else:
                number = p.value + q.value + 1
                print(number)
                remainder = False
        else:
            print(p.value+q.value)
            remainder = False
        p = p.prev
        q = q.prev
    if p is None and q is None and remainder:
        p = Node(1, None, p)
        print(p.value)


elem1 = Node(7, None,)
elem2 = Node(9, elem1)
elem1.next = elem2
elem_1 = Node(5, None,)
elem_2 = Node(1, elem_1)
elem_1.next = elem_2
add_two_numbers(elem1, elem_1)