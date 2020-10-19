from adt.list.ArrayList import ArrayList


class MinHeap(object):
    """
    Implementation d'un MinHeap avec un ArrayList
    """
    def __init__(self):
        self.__keys = ArrayList()

    def __len__(self):
        """
            Returns:
                retourne le nombre de node dans le heap
        """
        return len(self.__keys)

    def swapNodes(self, parent, child):
        """
        Change la position de deux node
            Args:
                parent: node a swap
                child: node a swap
        """
        temp = self.__keys[parent]
        self.__keys[parent] = self.__keys[child]
        self.__keys[child] = temp

    def get_parent(self, index):
        """
            Args:
                index: la position de la node fille
            Returns:
                retourne l'index de la node mère d'une node fille donnée

        """
        return index // 2

    def get_left(self, index):
        """
            Args:
                index: la position de la node mère
            Returns:
                retourne l'index de la node file gauche d'une node mère donnée

        """
        return index * 2

    def get_right(self, index):
        """
            Args:
                index: la position de la node mère
            Returns:
                retourne l'index de la node file droite d'une node mère donnée

        """
        return (index * 2) + 1

    def has_child(self, index):
        """
            Args:
                index: la position de la node mère
            Returns:
                retourne un boolean déterminant si la node mère possède des node filles

        """
        if self.get_left(index) >= len(self)-1 and self.get_right(index) >= len(self)-1:
            return False
        return True

    def insert(self, key):
        """
            Args:
                key: la clé a inserer dans le heap
        """
        self.__keys.add_back(key)
        index = len(self)-1
        while self.__keys[index] < self.__keys[self.get_parent(index)]:
            self.swapNodes(index, self.get_parent(index))
            index = self.get_parent(index)

    def transform_minheap (self):
        """
            appelle heapify pour rendre l'array conforme
        """
        for i in range(len(self)-1//2, 0, -1):
            self.heapify(i)

    def remove(self):
        """
            Returns:
                pop l'élément le plus petit du heap
        """
        to_remove = self.__keys[0]
        self.__keys[0] = self.__keys[len(self)-1]
        self.__keys.remove(len(self)-1)
        self.heapify(0)
        return to_remove

    def heapify(self, index):
        """ Swap de facons recursive les node d'un heap afin de les rendre conforme
            Args:
                index: la position dans le heap de départ
        """
        if self.has_child(index):
            if self.__keys[index] > self.__keys[self.get_left(index)] or self.__keys[index] > self.__keys[self.get_right(index)]:
                if self.__keys[self.get_left(index)] < self.__keys[self.get_right(index)]:
                    self.swapNodes(index , self.get_left(index))
                    self.heapify(self.get_left(index))
                else:
                    self.swapNodes(index , self.get_right(index))
                    self.heapify(self.get_right(index))
    def peek(self):
        """
            Returns:
                retourne l'élément le plus petit du heap
        """
        return self.__keys[0]

