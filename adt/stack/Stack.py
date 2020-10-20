from adt.list.LinkedList import LinkedList


class Stack:
    """
        Implémentation partielle d'un stack en utilisant un linked list.
    """

    def __init__(self):
        self.values = LinkedList()

    def push(self, value):
        return self.values.add_front(value)

    def pop(self):
        return self.values.remove_front()

    def is_empty(self):
        return self.values.is_empty()