"""
Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
struktury listy odsyłaczowej.
- czy element należy do zbioru
- wstawienie elementu do zbioru
- usunięcie elementu ze zbioru
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class List:
    def __init__(self):
        self.first = None

    def isthere(self, val):
        nextnode = self.first
        while (nextnode != None):
            if (nextnode.val == val):
                return True
            nextnode = nextnode.next
        return False

    def add(self, val):
        if (not self.isthere(val)):
            p = Node(val)
            p.next = self.first
            self.first = p

    def delete(self, val):
        if (self.first != None and self.first.val == val):
            self.first = self.first.next
        else:
            nextnode = self.first.next
            p = self.first
            while (nextnode != None):
                if (nextnode.val == val):
                    p.next = nextnode.next
                    return
                p = nextnode
                nextnode = nextnode.next

    def show(self):
        show_values = []
        nextnode = self.first
        while (nextnode != None):
            show_values.append(nextnode.val)
            nextnode = nextnode.next
        print(show_values)


lista = List()

lista.add(5)
lista.add(5)
lista.add(2)
lista.add(4)
lista.add(3)
lista.add(7)
lista.show()

lista.delete(3)
lista.show()
print(lista.isthere(4))
print(lista.isthere(3))
