from adt.list.ArrayList import ArrayList


class DescSortedList(ArrayList):
    """
    Implémentation contigue d'une liste ordonnée de façon descendante.
    """
    def __setitem__(self, key, value):
        raise NotImplementedError("La SortedListe assigne l'emplacement que prend un item. Utiliser push à la place.")

    def insert_at(self, item, index):
        raise NotImplementedError("La SortedListe assigne l'emplacement que prend un item. Utiliser push à la place.")

    def add_front(self, item):
        raise NotImplementedError("La SortedListe assigne l'emplacement que prend un item. Utiliser push à la place.")

    def add_back(self, item):
        raise NotImplementedError("La SortedListe assigne l'emplacement que prend un item. Utiliser push à la place.")

    def put(self, item, index):
        raise NotImplementedError("La SortedListe assigne l'emplacement que prend un item, alors nous ne pouvons pas modifier une valeur.")

    def push(self, item):
        """
        Permet d'inserer un item en dans la liste en préservant l'ordre de celle-ci.
        Args:
            item: L'item à ajouter dans la liste.
        """
        low = 0     #: Représente le plancher dans notre rayon de recherche
        high = len(self)-1  #: Représente le plafond dans notre rayon de recherche

        while low <= high:  #: Permet de s'assurer que nous passerons sur tous les items pertinants à la comparaison.
            mid = low + (high-low) // 2     #: Représente le centre de notre rayon de recherche. C'est à dire le plancher plus la moitié(arrondi à la baisse) de la distance entre le plancher et le plafond.
            if self.values[mid] < item:  #: Si la valeur à l'index milieu est inférieur que l'item à insérer, on baisse la plafond.
                high = mid - 1
            else:   #: Si la valeur à l'index milieu est supérieur que l'item à insérer, on monte le plancher.
                low = mid + 1
        self._grow()    #: On a ajuste la taille de la liste car on insère une valeur
        mid = low   #: le plafond et le plancher sont égaux, et représentent la positions à laquelle nous voulons insérer un item.
        for i in range(len(self) - 1, mid, -1):  #: En commençant par la nouvelle position vide qui a été ajoutée en créant la liste, on bouge toutes les valeurs vers la droite, jusqu'à ce qu'on arrive au point mid.
            self.values[i] = self.values[i - 1]
        self.values[mid] = item     #: On insère la nouvelle valeur au point mid.
        return

    def concat(self, other):
        """
            Ajouter les éléments d'une autre liste à la liste
            Args:
                other : Représente l'autre liste.
        """
        for element in other:
            self.push(element)
        return
