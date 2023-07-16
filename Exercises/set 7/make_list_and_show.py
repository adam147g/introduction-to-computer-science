class Node:
    def __init__(self):
        self.value = None
        self.next = None


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
    for i in range(len(T)-3,-1,-1):
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