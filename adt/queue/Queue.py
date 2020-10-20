from adt.list.ArrayList import ArrayList
from adt.list.LinkedList import LinkedList


class Queue():
    """
    Implémentation partielle d'un queue en utilisant un array list.
    """
    def __init__(self):
        self.values = LinkedList()

    def push(self, value):
        return self.values.add_back(value)

    def pop(self):
        return self.values.remove_front()

    def is_empty(self):
        return self.values.is_empty()
