"""
Zastosowanie listy odsyłaczowej do implementacji
tablicy rzadkiej. Proszę napisać trzy funkcje:
– inicjalizującą tablicę,
– zwracającą wartość elementu o indeksie n,
– podstawiającą wartość value pod indeks n.
"""

from random import randint


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self):
        node = Node(randint(1, 10), self.head)
        self.head = node

    def display_element(self, index, length):   # wyświetl element
        if self.head is None:
            print("List is empty")
            return
        if index < 0 or index >= length:
            return False
        count_idx = 0
        i = self.head
        while i is not None:
            if count_idx == index:
                return i.value
            i = i.next
            count_idx += 1


    def substitute_element(self, variable, index, length):  # podmiana na danym indeksie
        if index < 0 or index >= length:
            return False
        i = self.head
        count_idx = 0
        while i is not None:
            if count_idx == index:
                i.value = variable
                break
            i = i.next
            count_idx += 1


    def show(self):
        nextnode = self.head
        if(nextnode != None):
            print(nextnode.value, end = "")
        nextnode = nextnode.next
        while (nextnode != None):
            print(end = "->")
            print(nextnode.value, end = "")
            nextnode = nextnode.next
        print()


lista=LinkedList()
lista.add_at_beginning()
lista.add_at_beginning()
lista.add_at_beginning()
lista.add_at_beginning()
lista.add_at_beginning()
lista.add_at_beginning()
lista.show()

print(lista.display_element(2, 6))
lista.substitute_element(77, 3, 6)
lista.show()
