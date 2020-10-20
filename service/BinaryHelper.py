from adt.list.ArrayList import ArrayList


class BinaryHelper:
    """
    Classe permettant de transformer du code binaire (sous forme de string) en bytes et vice versa.
    """
    def __init__(self):
        pass

    def make_byte_array(self, bits):
        """
        Méthode qui converti des des bits en plusieurs bytes.
        Args:
            bits: Chaine contenant tous les bits ex: 1010101011111

        Returns:
            Un array de bytes.
        """
        pos = 0     #: Les string ne peuvent pas être modifié alors je l'indexe.
        byte_array = ArrayList()    #:  Array pour stocker tous mes bytes.
        while pos < len(bits):  #: Aussi longtemps que je n'ai pas parcouru le string au complet.
            count = 8   #: On commence toujours à 8 car 8bits per byte.
            byte = 0    #: Valeur du byte courant.
            while pos < len(bits) and count > 0:    #: Aussi longtemps que je n'ai pas un byte complet ou que le tableau n'est pas vide, je converti les bits en décimal.
                current_bit = bits[pos]
                pos += 1
                count -= 1
                if current_bit == '1':
                    byte += 2 ** count
            byte_array.add_back(byte)   #:  J'ajoute les byte à la fin toujours, car je veux qu'ils soient en ordre de lecture.git st
        return bytearray(byte_array)
