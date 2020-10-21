from adt.list.IList import IList


class Node(object):
    """ Noeud d'un LinkedList
        Args:
            item(object): l'item qui est storé dans le noeud
            next_node(Node): Le noeud suivant le noeud courant

    """
    def __init__(self, item, next_node=None):
        self.item = item
        self.next_node = next_node


class LinkedList(IList):
    """ Implémentation à deux têtes d'une liste chaînée
        Attributes:
            head(Node): l'item qui est à la tête de la liste.
            tail(Node): l'item qui est à la queue de la liste.
    """
    def __init__(self):
        self.__head = None
        self.__tail = None

    def __getitem__(self, index):
        """
            Args:
                index (int): Représente la positions à laquelle nous recherchons un élément dans la liste.
            Returns:
                L'élément à la position de l'index ou None si la case est vide.
            Raises:
                IndexError: Si l'index n'est pas à une position qui existe dans la liste.
        """
        return self.get(index)

    def __len__(self):
        """
        Returns:
            Le nombre d'éléments contenus dans la liste.
        """
        counter = 0
        node = self.__head
        while node:
            counter += 1
            node = node.next_node
        return counter

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
            self.put(value,key)
        return

    def __str__(self):
        """
            Returns:
                Une chaîne de caractères qui représente toutes les valeurs contenues dans la liste.
        """
        string = "["  #: Premier caractère de la liste est un [
        for i in iter(self):
            string += f"{i}, "  #: Ajoute chaque item sauf le dernier suivi d'une virgule et d'un espace.
        string = f"{string[:-2]}]"  #: Met une accolade fermente apres le dernier item.
        return string

    def insert_at(self, item, index):
        """ Insére un item à un certain index de la liste.
            Args:
                item (object): L'item qui sera inséré.
                index (int): L'index auquel cet item sera inséré.
         """
        if not 0 <= index <= len(self):
            raise IndexError('Provided index is out of bounds')

        previous_node = None    #: On garde le noeud précédent en mémoire car ça facilite les transformations sur le noeud courant.
        current_node = self.__head  #: On commence à la tête.

        if index == 0:  #: Permet de modifier le head si l'index est 0.
            self.__head = Node(item, self.__head)
            if self.__tail is None:     #: Initialiser la queue si ce n'est pas déjà fait.
                self.__tail = self.__head
            return
        #:  Cette partie du code s'éxécute si nous n'avions pas modifier la tête de la liste.
        counter = 0

        while counter < index:  #: On trouve le noeud à modifier en passant de parent à enfant.
            counter += 1
            previous_node = current_node
            current_node = current_node.next_node

        previous_node.next_node= Node(item, current_node)   #: On ajoute le nouveau noeud a la place du noeud courant et on met celui-ci comment enfant du nouveau noeud.

    def add_back(self, item):
        """ Ajoute un item à la queue de la liste
            Args:
                item (object): L'item que nous insérons dans la liste.
        """
        if self.__head is None: #: Initialise la tête et la queue si la liste était vide.
            self.__head = Node(item)
            self.__tail = self.__head
            return
        #: Cette partie du code s'éxécute si la liste n'était pas vide.
        self.__tail.next_node = Node(item)  #: On ajoute un enfant à la queue et la queue devient cet enfant.
        self.__tail = self.__tail.next_node
        return

    def add_front(self, item):
        """ Ajoute un item à la tête de la liste
            Args:
                item (object): The item to be inserted in the list.
        """
        return self.insert_at(item, 0)

    def remove(self, index):
        """ Retire un élément de la liste à un index donné.
            Args:
                index (int): L'index de l'item a retiré.
            Returns:
                L'item qui a été retiré.
        """
        if not 0 <= index < self.length():
            raise IndexError('Index hors des limites de la liste.')
        previous_node = None    #: On garde le noeud précédent en mémoire car ça facilite les transformations sur le noeud courant.
        current_node = self.__head

        if index == 0:  #: Si l'index est 0 on retire la tête
            to_return = self.__head.item
            self.__head = self.__head.next_node
            return to_return
        #: Ce code s'éxécute si l'index n'était pas 0
        counter = 0
        #: On trouve la position et on la remplace par son prochain noeud.
        while counter < index:
            counter += 1
            previous_node = current_node
            current_node = current_node.next_node
        to_return = current_node
        previous_node.next_node = None
        return to_return.item

    def remove_back(self):
        """ Retire la queue de la liste
            Returns:
                Retourne la valeur qui a été retirée.
        """
        return self.remove(len(self)-1)

    def remove_front(self):
        """Retire la tête de la liste
            Returns:
                Retourne la valeur qui a été retirée.
        """
        return self.remove(0)

    def get(self, index):
        """
        Args:
            index (int): Représente la positions à laquelle nous recherchons un élément dans la liste.
        Returns:
            L'élément à la position de l'index ou None si la case est vide.
        Raises:
            IndexError: Si l'index n'est pas à une position qui existe dans la liste.
        """
        if not 0 <= index < self.length():
            return IndexError('Provided index is out of bounds')
        counter = 0
        current_node = self.__head
        #: On trouve le noeud et on le renvoit.
        while counter < index:
            counter += 1
            current_node = current_node.next_node
        return current_node.item

    def put(self, item, index):
        """ Remplacer un item dans la liste par un nouvel item.
            Args:
                item (object): Le nouvel item.
                index (int): L'index de l'item que nous voulons remplacer.
        """
        if not 0 <= index < self.length():
            return IndexError('Provided index is out of bounds')
        counter = 0
        current_node = self.__head
        #: On trouve l'item et on change sa valeur.
        while counter is not index:
            counter += 1
            current_node = current_node.next_node
        current_node.item = item
        return

    def find(self, item):
        """ Trouver l'index de la première occurence d'un item.
            Args:
                item (object): L'item qu'on veut trouver dans la liste..
            Returns:
                Retourne l'index de l'item que nous cherchons ou -1 si on ne le trouve pas.
        """
        current_node = self.__head
        counter = 0
        while current_node is not None:
            if current_node.item is item:
                return counter
            counter += 1
            current_node = current_node.next_node
        return -1

    def concat(self, other):
        """ Permet de concaténer une autre liste à celle-ci.
            Args:
                other (IList): L'autre liste qui sera ajoutée.
        """
        for i in other:
            self.add_back(i)
        return

    def length(self):
        """
            Returns:
                La longueure de la liste.
        """
        return len(self)

    def is_empty(self):
        """
            Returns:
                True si la liste est vide, False sinon.
        """
        if self.__head is None:
            return True
        return False

    def __iter__(self):
        """
        Permet d'itérer au travers de notre liste.
        Yields:
            Chaque valeur en ordre, de notre linked list.
        """
        current_node = self.__head
        while current_node is not None:
            yield current_node.item
            current_node = current_node.next_node