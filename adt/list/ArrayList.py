import ctypes

from adt.list.IList import IList


class ArrayList(IList):
    """
    Implémentation contigue d'une liste.
    Attributes:
        length (int): Représente le nombre d'éléments contenus dans la liste.
        capacity (int): Représente la taille du tableau.
        values ([]): Représente le tableau sur lequel la liste repose.
    """
    def __init__(self, capacity=100):
        self.length = 0
        self.capacity = capacity
        #: Permet d'initialiser un array de taille capacity.
        self.values = ArrayList._build_array(self.capacity)

    def __len__(self):
        """
        Returns:
            Le nombre d'éléments contenus dans la liste.
        """
        return self.length

    def __getitem__(self, index):
        """
        Args:
            index (int): Représente la positions à laquelle nous recherchons un élément dans la liste.
        Returns:
            L'élément à la position de l'index ou None si la case est vide.
        Raises:
            IndexError: Si l'index n'est pas à une position qui existe dans la liste.
        """
        if 0 > index or index >= self.length:
            raise IndexError
        try:
            return self.values[index]
        except ValueError:
            return None

    def __setitem__(self, key, value):
        """
        Modifier la valeur d'un élément à une position spécifique dans la liste.
        Args:
            key (int): Représente la position où nous voulons mettre la valeur.
            value : Représente l'item que nous voulons mettre à cette position.
        Raises:
            IndexError: Si l'index n'est pas à une position qui existe dans la liste.
        """
        if 0 > key or key > len(self):
            raise IndexError
        else:
            self.values[key] = value
        return

    def __str__(self):
        """
        Returns:
            Une chaîne de caractères qui représente toutes les valeurs contenues dans la liste.
        """
        string = "["    #: Premier caractère de la liste est un [
        for i in range(len(self) - 1):
            string += f"{self.get(i)}, "    #: Ajoute chaque item sauf le dernier suivi d'une virgule et d'un espace.
        string += f"{self.get(len(self) - 1)}]"    #: Ajoute le dernier item avec une accolade fermente.
        return string

    @staticmethod
    def _build_array(capacity):
        """
        Construction d'un tableau
        Args:
            capacity (int) : Taille désirée du tableau.
        Returns:
            Un tableau de la taille "capacity"
        """
        return [None] * capacity

    def _grow(self):
        """
        Gère la taille du tableau et la valeur de length lors de l'insertion dans le tableau.
        """
        if len(self) == self.capacity:  #: Si le tableau est plein, recréer un tableau avec 100 cases de plus.
            self.capacity += 100
            new_array = ArrayList._build_array(self.capacity)
            for i in range(len(self)):
                new_array[i] = self.values[i]
            self.values = new_array
        self.length += 1    #: Augmenter la taille de la liste de 1.
        return

    def insert_at(self, item, index):
        """
        Ajouter un élément à une positions spécifique dans la liste.
        Args:
            index (int): Représente la position où nous voulons mettre la valeur.
            item : Représente l'item que nous voulons mettre à cette position.
        Raises:
            IndexError: Si l'index n'est pas à une position qui existe dans la liste.
        """
        self._grow()  #: Augmente la taille de la liste car nous allons insérer un item.
        if 0 > index or index > len(self):
            raise IndexError
        else:
            old_value = self[index]  #: Sauvegarde la valeur à la position "index"
            self[index] = item   #: Donne la nouvelle valeur à la position "index"
            for i in range(index + 1, len(self)):  #: Parcours la liste à partir de la valeur après l'index et bouge les valeurs vers la droite.
                tmp = self[i]
                self[i] = old_value
                old_value = tmp
        return

    def add_front(self, item):
        """
        Ajouter un élément au début de la liste.
        Args:
            item : Représente l'item que nous voulons insérer.
        """
        return self.insert_at(item, 0)

    def add_back(self, item):
        """
        Ajouter un élément à la fin de la liste.
        Args:
            item : Représente l'item que nous voulons insérer.
        """
        return self.insert_at(item, len(self))

    def remove(self, index):
        """
        Retirer un élément d'un position de la liste.
        Args:
            index (int) : Représente la position de l'élément que nous voulons retirer.
        Returns:
            L'élément qui a été supprimé.
        Raises:
            IndexError: Si l'index n'est pas à une position qui existe dans la liste.
        """
        if 0 > index or index > len(self):
            raise IndexError
        else:
            to_return = self[index]
            for i in range(index, len(self)-1):
                if self.values[i+1]:
                    self.values[i] = self.values[i+1]
            self.length -= 1
        return to_return

    def remove_front(self):
        """
        Retirer un élément du début de la liste.
        """
        return self.remove(0)

    def remove_back(self):
        """
        Retirer un élément de la fin de la liste.
        """
        return self.remove(len(self)-1)

    def get(self, index):
        """
        Retourner un élément à une position spécifique de la liste.
        Args:
            index (int) : Représente la position de l'élément que nous voulons renvoyer.
        Returns:
            L'élément à cette position.
        """
        return self[index]

    def put(self, item, index):
        """
        Remplace l'élément à la position index avec l'élément item.
        Args:
            index (int) : Représente la position de l'élément que nous voulons remplacer.
            item : Représente l'élément avec lequel nous voulons remplacer l'ancien.
        """
        self[index] = item
        return

    def find(self, item):
        """
        Trouver l'élément item dans la liste.
        Args:
            item : Représente l'élément que nous recherchons.
        Returns:
            Retourne la position de l'élément s'il est trouvé ou -1 s'il n'est pas trouvé.
        """
        for i in range(len(self)):
            if self[i] == item:
                return i
        return -1

    def concat(self, other):
        """
        Ajouter les éléments d'une autre liste à la liste
        Args:
            other : Représente l'autre liste.
        """
        for element in other:
            self.add_back(element)
        return

    def length(self):
        """
        Returns:
            La longueur de la liste
        """
        return len(self)

    def is_empty(self):
        """
        Vérifier si la liste est vide
        Returns:
            True si la liste est vide, False si elle ne l'est pas
        """
        if len(self) == 0:
            return True
        return False

    def __iter__(self):
        for i in range(len(self)-1):
            yield self[i]