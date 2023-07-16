"""
Proszę napisać funkcję scalającą dwie posortowane listy w jedną
posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
- funkcja iteracyjna,
- funkcja rekurencyjna.
"""

class Node:
    def __init__(self):
        self.value = None
        self.next = None


# 1ST SOLUTION ITERATION

def iteration_merge(p1, p2):
    f = Node()
    last = f
    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            last.next = p1
            last = p1
            p1 = p1.next
        else:
            last.next = p2
            last = p2
            p2 = p2.next
    if p1 is not None:
        last.next = p1
    else:
        last.next = p2
    return f.next


# 2ND SOLUTION RECURSION

def recursion_merge(p1, p2):
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    if p1.value < p2.value:
        result = p1
        result.next = recursion_merge(p1.next, p2)
    else:
        result = p2
        result.next = recursion_merge(p1, p2.next)
    return result




def make_list(T):
    if len(T) == 0:
        return None
    tail = Node()
    tail.value = T[-1]
    if len(T) == 1:
        return head
    node = Node()
    node.value = T[-2]
    node.next = tail
    for i in range(len(T)-3, -1, -1):
        nextnode = node
        node = Node()
        node.value = T[i]
        node.next = nextnode
    return node

def show(p):
    while p.next is not None:
        print(p.value, end="->")
        p = p.next
    print(p.value)


T_1 = [1, 2, 3, 10, 14, 18, 19]
p_1 = make_list(T_1)
show(p_1)
T_2 = [0, 4, 6, 11, 12, 13, 20]
p_2 = make_list(T_2)
show(p_2)

res_iter = iteration_merge(p_1,p_2)
show(res_iter)
print()
T_1 = [1, 2, 3, 10, 14, 18, 19]
p_1 = make_list(T_1)
show(p_1)
T_2 = [0, 4, 6, 11, 12, 13, 20]
p_2 = make_list(T_2)
show(p_2)
res_rec = recursion_merge(p_1,p_2)
show(res_rec)