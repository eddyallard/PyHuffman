import ctypes


class HashEntry(object):
    def __init__(self, key=None, item=None, deleted=False):
        """
            Couple de clé/valeur pour la table de hashage
                Args:
                    key : Représente la clé du couple clé/valeur. Doit être unique
                    item : Représente la valeur du couple clé/valeur
                    deleted : Flag permettant de savoir si ce couple clé/valeur est encore valide
        """
        self.key = key
        self.item = item
        self.deleted = deleted

    def __str__(self):
        return f"{self.key, self.item}"


class HashTable(object):
    """
        Implémentation d'une Hashtable en adressage ouvert
            Args:
                capacity : Représente la capacité maximale de la table de hashage
                table = Représente la table de hashage sous forme d'un array de taille fixe
                size = Représente le nombre de HashEntry valide dans la table
    """
    def __init__(self, capacity=100):
        self.__capacity = capacity
        self.__table = HashTable.__initialise_array(capacity)
        self.size = 0

    def __len__(self):
        """Retourne le nombre de HashEntry valide dans la table"""
        return self.size

    @staticmethod
    def build_array(new_capacity):
        """
        Permet l'initialisation de la table
            Args:
                new_capacity : Représente la capacité maximale de la table de hashage
            Returns:
                retourne un tableau vide de capacité new_capacity
        """
        return (new_capacity * ctypes.py_object)()

    @staticmethod
    def __initialise_array(new_capacity):
        """
        Permet l'initialisation de la table
            Args:
                new_capacity : Représente la capacité maximale de la table de hashage
            Returns:
                retourne un tableau None
        """
        table = HashTable.build_array(new_capacity)
        for i in range(0, new_capacity - 1):
            table[i] = None
        return table

    @staticmethod
    def is_free(entry):
        """
        Permet l'initialisation de la table
            Args:
                entry : Représente une case dans la table de hachage (soit None ou HashEntry)
            Returns:
                retourne un vrai si l'entry est vide ou deleted, retourne faux autrement
        """
        if entry is None:
            return True
        if entry.deleted:
            return True
        return False

    @staticmethod
    def hash(key):
        """
        Permet le hashage des clé
            Args:
                key : Représente une clé sous la forme d'un char
            Returns:
                retourne le mod 29 de la valeur ASCII du char
        """
        hashed_key = 0
        for i in range(len(key)):
            if key[i] == 1:
                hashed_key += 2 ^ i
        return hashed_key

    def __setitem__(self, key, item):
        """
        Permet d'insérer un HashEntry dans la table
            Args:
                key : Représente une clé sous la forme d'un char
                item: Représente une valeur
        """
        index = self.hash(key)
        for i in range(index, self.__capacity - 1, 1):
            if self.is_free(self.__table[i]):
                self.__table[i] = HashEntry(key, item)
                self.size += 1
                return
        print("there is no space left")

    def remove(self, key):
        """
        Permet de Flag un HashEntry en mode deleted
            Args:
                key : Représente une clé sous la forme d'un char
        """
        index = HashTable.hash(key)
        for i in range(index, self.__capacity - 1, 1):
            if self.is_free(self.__table[i]) is False:
                if self.__table[i].key == key:
                    self.__table[index].deleted = True
                    self.size -= 1
                    return
        raise KeyError(f"Pas de clée {key}.")

    def __getitem__(self, key):
        """
        Permet de Flag un HashEntry en mode deleted
            Args:
                key : Représente une clé sous la forme d'un char
            Returns:
                retourne la valeur correspondante
        """
        index = self.hash(key)
        for i in range(index, self.__capacity - 1, 1):
            if self.is_free(self.__table[i]) is False:
                if self.__table[i].key == key:
                    return self.__table[i].item
        raise KeyError(f"Pas de clée {key}.")
