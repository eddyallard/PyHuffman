from adt.list.LinkedList import LinkedList


class Stack:
    """
        Implémentation partielle d'une pile en utilisant un linked list.
    """

    def __init__(self):
        self.values = LinkedList()

    def push(self, value):
        """
        Ajoute une valeur au dessus de la pile.
        Args:
            value: La valeur que nous voulons ajouter.
        """
        return self.values.add_front(value)

    def pop(self):
        """
        Retirer une valeur du dessus de la pile.
        Returns:
            La valeur qui a été retirée.
        """
        return self.values.remove_front()

    def is_empty(self):
        """
            Returns:
                True si la pile est vide, False sinon.
        """
        return self.values.is_empty()