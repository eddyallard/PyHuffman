from adt.list.ArrayList import ArrayList
from adt.list.LinkedList import LinkedList
from adt.stack.Stack import Stack


class BinaryHelper:
    """
    Classe permettant de transformer du code binaire (sous forme de string) en bytes et vice versa.
    """
    def __init__(self):
        pass

    def to_int(self, bits: ArrayList):
        """
        Méthode permettant de transformer un ArrayList de bits en un int.
        Args:
            bits: Liste de bits sous forme de strings donc '0' ou '1'

        Returns:
            La valeur en int de cette liste.
        """
        value = 0
        for i in range(len(bits)):
            value += (int(bits[i]) * (2 ** (7-i)))
        return value

    def to_bits(self, number: int):
        """
        Méthode permettant de transformer un int en un byte sous forme binaire ex : '10011010'
        Args:
            number: Le nombre a convertir

        Returns:
            La representation sous forme de chaine du code binaire.
        """
        bit = ''
        current_byte = Stack()  #: On utilise un stack car on calcule le binaire en faisant les modulos, cela nous donne la réponse à l'envers.
        cnt = 0
        while cnt < 8:
            current_byte.push(f"{number % 2}")
            number = number // 2
            cnt += 1
        while not current_byte.is_empty():
            bit += current_byte.pop()
        return bit
