import ctypes


class HashEntry(object):
    def __init__(self, key=None, item=None):
        """
            Couple de clé/valeur pour la table de hashage
                Args:
                    key : Représente la clé du couple clé/valeur. Doit être unique
                    item : Représente la valeur du couple clé/valeur
        """
        self.key = key
        self.item = item

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
    def __init__(self, capacity=256):   #: Tableau de taille 256, car nous ne l'utilisons que pour le huffdata et comme nous sommes en utf8, il y a 256 valeurs possibles.
        self.__capacity = capacity
        self.__table = self.__initialise_array(capacity)
        self.size = 0

    def __len__(self):
        """Retourne le nombre de HashEntry valide dans la table"""
        return self.size

    def build_array(self, new_capacity):
        """
        Permet l'initialisation de la table
            Args:
                new_capacity : Représente la capacité maximale de la table de hashage
            Returns:
                retourne un tableau vide de capacité new_capacity
        """
        return (new_capacity * ctypes.py_object)()

    def __initialise_array(self, new_capacity):
        """
        Permet l'initialisation de la table
            Args:
                new_capacity : Représente la capacité maximale de la table de hashage
            Returns:
                retourne un tableau de taille new_capacity, où chaque case est initialisé à None.
        """
        table = self.build_array(new_capacity)     #: Crée le tableau vide.
        for i in range(0, new_capacity - 1):    #: Itère le tableau pour initialiser chaque valeur à None.
            table[i] = None
        return table

    def is_free(entry):
        """
        Permet l'initialisation de la table
            Args:
                entry : Représente une case dans la table de hachage (soit None ou HashEntry)
            Returns:
                retourne un vrai si l'entry est vide, retourne faux autrement
        """
        if entry is None:
            return True
        return False

    def hash(key):
        """
        Permet le hashage des clés. Dans notre cas, comme nous savons que les clés seront un code binaire,
        notre méthode de hachage ne fait que transposer le string de code binaire en décimal. De cette façon nous
        évitons les collisions, car les codes binaires ne se répèteront jamais.
            Args:
                key : La clé
            Returns:
                retourne la clée qui a été hachée.
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
        index = self.hash(key)  #: On commence par Hash la clée.
        for i in range(index, self.__capacity - 1, 1):  #: Ensuite on regarde dans le hashtable s'il y a de la place à cet endroit. Sinon, on navigue à droite jusqu'à ce qu'il y ait une place.
            if self.is_free(self.__table[i]):
                self.__table[i] = HashEntry(key, item)
                self.size += 1
                return
        raise ValueError("Il n'y a plus d'espace dans le HashTable pour cette clé.")

    def remove(self, key):
        """
        Permet de Flag un HashEntry en mode deleted
            Args:
                key : Représente une clé sous la forme d'un char
            Returns:
                La valeur que nous avons retiré.
        """
        index = self.hash(key)
        for i in range(index, self.__capacity - 1, 1):
            if self.is_free(self.__table[i]) is False:
                if self.__table[i].key == key:
                    to_remove = self.__table[index]
                    self.__table[index] = None
                    self.size -= 1
                    return to_remove
        raise KeyError(f"Pas de clée {key}.")

    def __getitem__(self, key):
        """
        Permet de Flag un HashEntry en mode deleted
            Args:
                key : Représente la clé
            Returns:
                retourne la valeur correspondante
        """
        index = self.hash(key)
        for i in range(index, self.__capacity - 1, 1):
            if self.__table[i].key == key:
                return self.__table[i].item
        raise KeyError(f"Pas de clée {key}.")
