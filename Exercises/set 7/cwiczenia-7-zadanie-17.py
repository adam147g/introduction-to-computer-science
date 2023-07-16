"""
Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
początek listy dwukierunkowej, usuwa z niej wszystkie elementy, w których
wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek.
"""

class Node:
    def __init__(self, value=None, prev=None, next_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev


def base_convert(number, base=2):
    a = ""
    hex = "0123456789ABCDEF"
    while number > 0:
        a = hex[number % base] + a
        number = number // base
    return int(a)


def count_digits(number):
    one_count = 0
    while number != 0:
        c = number % 10
        number //= 10
        if c == 1:
            one_count += 1
    if one_count % 2 == 1:
        return True
    return False


def remove_binary_numbers(first):
    p = first
    r = p.prev
    q = p.next
    if first is None:
        return None
    while q is not None:
        converted_p = base_convert(p.value)
        if count_digits(converted_p):
            p = r
            p = q
            q = p.next
        else:
            r = p
            p = p.next
            q = p.next
    if p is not None:
        converted_p = base_convert(p.value)
        if count_digits(converted_p):
            p = r
        p = q


elem1 = Node(7)
elem2 = Node(5, elem1)
elem1.next = elem2
elem3 = Node(4, elem2)
elem2.next = elem3
elem4 = Node(7, elem3)
elem3.next = elem4
remove_binary_numbers(elem1)
