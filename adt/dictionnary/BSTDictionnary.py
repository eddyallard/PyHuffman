from adt.list.ArrayList import ArrayList


class Entry:
    """
    Une entrée du dictionnaire.
    Attributes:
        key : Clé de l'entrée.
        value : Valeur associées à la clé.
    """
    def __init__(self, key, value=None):
        self.key = key
        self.value = value


class BSTNode:
    """
    Un noeud de l'arbre.
    Attributes:
        entry : L'item qui est storé dans le noeud.
        left_child : L'enfant de gauche de ce noeud.
        right_child : L'enfant de droite de ce noeud.
    """
    def __init__(self, entry=None):
        self.entry = entry
        self.left_child = None
        self.right_child = None


class BSTDict:
    """
    Implémentation itérative d'un dictionnaire utilisant la structure d'un Arbre de Recherche Binaire.
    Attributes:
        root (BSTNode): Root node of the tree
    """
    def __init__(self):
        self.root = BSTNode(None)

    def __setitem__(self, key, value):
        """
        Insertion ou modification d'une valeur dans le BSTDict.
        Args:
            key : Représente la clé que nous voulons insérer ou modifier.
            value : Représente la valeur que nous voulons associer à cette clé.
        """
        if not self.root.entry or self.root.entry.key == key:   #: Si la racine n'a pas d'entry, on lui en donne une et l'appel de la méthode est achevé.
            self.root.entry = Entry(key, value)
            return
        #: Cette partie du code est atteinte si la racine était existante.
        current_node = self.root
        while current_node:     #:Aussi longtemps que le noeud courant existe nous parcourons l'arbre.
            if current_node.entry.key < key:    #: Si la clé de l'entrée du noeud courant est plus petite que le clé que nous voulons modifier/insérer, on navigue à droite.
                previous_node = current_node
                current_node = current_node.right_child
            elif current_node.entry.key > key:  #: Si la clé de l'entrée du noeud courant est plus grande que le clé que nous voulons modifier/insérer, on navigue à gauche.
                previous_node = current_node
                current_node = current_node.left_child
            else:   #: Si la clé est trouvée, sa valeur est modifiée
                current_node.entry.value = value
                return
        #: Cette partie du code est atteinte si la clé n'est pas trouvée
        if previous_node.entry.key < key:   #: Si la clé de l'entrée du noeud précédant est plus petite que le clé que nous voulons modifier/insérer, on insère le nouveau noeud à droite.
            previous_node.right_child = BSTNode(Entry(key, value))
        else:   #: Si la clé de l'entrée du noeud précédant est plus grande que le clé que nous voulons modifier/insérer, on insère le nouveau noeud à gauche.
            previous_node.left_child = BSTNode(Entry(key, value))
        return

    def __getitem__(self, key):
        """
            Récupération d'une valeur dans le BSTDict selon la clé.
            Args:
                key : Représente la clé que nous voulons récupérer.
            Raises
                KeyError : si la clé n'existe pas.
        """
        current_node = self.root
        while current_node:     #:Aussi longtemps que le noeud courant existe nous parcourons l'arbre.
            if current_node.entry.key < key:    #: Si la clé de l'entrée du noeud courant est plus petite que le clé que nous voulons récupérer, on navigue à droite.
                current_node = current_node.right_child
            elif current_node.entry.key > key:  #: Si la clé de l'entrée du noeud courant est plus grande que le clé que nous voulons récupérer, on navigue à gauche.
                current_node = current_node.left_child
            else:   #: Si la clé est retrouvée, on renvoie sa valeur.
                return current_node.entry.value
        #: Cette partie du code s'éxecute si la clé n'est pas trouvée
        raise KeyError

    def __delitem__(self, key):
        """"
            Suppression d'une entrée dans le BST selon la clé.
            Args:
                key : Représente la clé de l'entrée que nous voulons supprimer.
            Raises
                KeyError : si la clé n'existe pas.
        """
        previous_node = None    #: On doit garder le noeud précédent le noeud courant en mémoire pour permettre la persistance des modifications.
        current_node = self.root
        while current_node:     #: Aussi longtemps que le noeud courant existe nous parcourons l'arbre.
            if current_node.entry.key < key:    #: Si la clé de l'entrée du noeud courant est plus petite que le clé que nous voulons supprimer, on navigue à droite.
                previous_node = current_node
                current_node = current_node.right_child
            elif current_node.entry.key > key:  #: Si la clé de l'entrée du noeud courant est plus petite que le clé que nous voulons supprimer, on navigue à gauche.
                previous_node = current_node
                current_node = current_node.left_child
            else:   #: Si la clé est trouvée, nous entrons dans l'étape de suppression
                if (not current_node.left_child and not current_node.right_child) or ((current_node.left_child or current_node.right_child) and not (
                        current_node.left_child and current_node.right_child)):  #: Si le noeud à supprimer a au plus un enfant.
                    if current_node.left_child:     #Si cet enfant est à gauche, le nouvelle valeur que prendra ce noeud est celle de cet enfant.
                        new_node_value = current_node.left_child
                    else:   #: Si cet enfant est à droite, le nouvelle valeur que prendra ce noeud est celle de cet enfant, autrement, la valeur de l'enfant à droite sera None, dans le cas ou le noeud n'a aucun enfant.
                        new_node_value = current_node.right_child
                    if previous_node:   #: Si le noeud a un previous_node(si ce n'est pas la racine), on modifie l'enfant approprié de ce noeud parent.
                        if previous_node.entry.key < key:
                            previous_node.right_child = new_node_value
                        else:
                            previous_node.left_child = new_node_value
                    else:   #: Autrement le noeud est la racine alors on modifie tout simplement la valeur de celle-ci directement.
                        self.root = new_node_value
                    return
                #: Cette partie du code s'exécute si le noeud a deux enfants.
                #: Dans ce cas, nous ne faisons que modifier l'entrée de ce noeud avec celle de la plus petit entrée dans sont sous arbre de droite.
                leftmost_node_entry = self.pop_leftmost(current_node.right_child)    #: On va chercher la plus petite entrée de l'arbre de droite et on supprime .
                if previous_node:   #: Si le noeud a un previous_node(si ce n'est pas la racine), on modifie l'enfant approprié de ce noeud parent.
                    if previous_node.entry.key < key:  #:Assignation
                        previous_node.right_child.entry = leftmost_node_entry
                    else:
                        previous_node.left_child.entry = leftmost_node_entry
                else:
                    self.root.entry = leftmost_node_entry
                return  #: Autrement le noeud est la racine alors on modifie tout simplement la valeur de celle-ci directement.
        #: Cette partie du code s'éxecute si la clé n'est pas trouvée
        raise KeyError

    def pop_leftmost(self, root=None):
        """"
            Suppression de la plus petite entrée dans le BST ou le sous arbre.

            Args:
                root : Représente le noeud auquel nous voulons retirer l'item le plus à petit.
            Returns:
                L'entrée du noeud qui est supprimé.
            Raises
                KeyError : si l'arbre est vide'.
        """
        if not root and self.root:  #: Si aucun noeud de départ est assigné, on commence à la racine de l'arbre
            root = self.root
        else:
            raise KeyError("Tree empty")
        previous_node = None
        current_node = root
        while current_node.left_child:  #: Tant qu'il y a des noeuds plus à gauche dans l'arbre, on parcourt celui-ci
            previous_node = current_node
            current_node = current_node.left_child
        to_return = current_node.entry  #: On sauvegarde l'entrée du noeud que nous supprimons
        #: Comme c'est le dernier noeud à gauche, c'est impossible qu'il ait 2 enfants alors nous n'avons qu'à prendre la valeur de son enfant ou None s'il en a aucun.
        if current_node.left_child:  # Si cet enfant est à gauche, le nouvelle valeur que prendra ce noeud est celle de cet enfant.
            new_node_value = current_node.left_child
        else:  #: Si cet enfant est à droite, le nouvelle valeur que prendra ce noeud est celle de cet enfant, autrement, la valeur de l'enfant à droite sera None, dans le cas ou le noeud n'a aucun enfant.
            new_node_value = current_node.right_child
        if previous_node:  #: Si le noeud a un previous_node(si ce n'est pas la racine), on modifie l'enfant approprié de ce noeud parent.
            if previous_node.entry.key < to_return.key:
                previous_node.right_child = new_node_value
            else:
                previous_node.left_child = new_node_value
        else:  #: Autrement le noeud est la racine alors on modifie tout simplement la valeur de celle-ci directement.
            self.root = new_node_value
        return to_return

    def inorder(self):
        """
        Parcours l'arbre en ordre croissant.

        Retourne: Les noeuds en ordre sous forme de liste
        """
        return self.__inorder(self.root, ArrayList())

    def __inorder(self, node, data: ArrayList()):
        """
        Parcours l'arbre en ordre croissant.

        Retourne: Les noeuds en ordre sous forme de liste
        """
        if node:
            self.__inorder(node.left_child, data)
            data.add_back(node.entry)
            self.__inorder(node.right_child, data)
        return data




