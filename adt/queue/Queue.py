from adt.list.ArrayList import ArrayList
from adt.list.LinkedList import LinkedList


class Queue():
    """
    Implémentation partielle d'une file en utilisant un linked list.
    """
    def __init__(self):
        self.values = LinkedList()

    def push(self, value):
        """
        Ajoute une valeur à l'arrière du Queue.
        Args:
            value: La valeur que nous voulons ajouter.
        """
        return self.values.add_back(value)

    def pop(self):
        """
        Retire l'item à l'avant de la file.
        Returns:
            La valeur qui a été retirée.
        """
        return self.values.remove_front()

    def is_empty(self):
        """
            Returns:
                True si la file est vide, False sinon.
        """
        return self.values.is_empty()

