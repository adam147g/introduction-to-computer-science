"""
Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
początek listy jednokierunkowej, usuwa z niej wszystkie elementy, w których
wartość klucza w zapisie trójkowym ma większą ilość jedynek niż dwójek.
"""

from make_list_and_show import make_list, show

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def base_convert(number):
    a = ""
    hex = "0123456789ABCDEF"
    while number > 0:
        a = hex[number % 3] + a
        number = number // 3
    return int(a)


def count_digits(number):
    one_count = 0
    two_count = 0
    while number != 0:
        c = number % 10
        number //= 10
        if c == 1:
            one_count += 1
        if c == 2:
            two_count += 1
    return one_count, two_count


def remove_key_elements(first):
    if first is None:
        return None
    while first is not None:
        converted = base_convert(first.value)
        digits = count_digits(converted)
        if digits[0] > digits[1]:
            first = first.next
        else:
            break
    p = first
    q = p.next
    while p is not None and q is not None:
        converted = base_convert(q.value)
        digits = count_digits(converted)
        if digits[0] > digits[1]:
            q = q.next
            p.next = q
        else:
            p = q
            q = q.next
    return first

T = [1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
p = make_list(T)
show(p)
p = remove_key_elements(p)
show(p)