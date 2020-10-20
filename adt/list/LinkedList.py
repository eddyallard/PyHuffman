from adt.list.IList import IList


class Node(object):
    """ Node object for LinkedList
        Args:
            item(object): item to be stored
            nextNode(Node): The next node in the list, can be None

    """
    def __init__(self, item, next_node=None):
        self.item = item
        self.next_node = next_node


class LinkedList(IList):
    """ Singly LinkedList implementation with two head"""
    def __init__(self):
        self.__head = None
        self.__tail = None

    def __len__(self):
        """ count all nodes in the list
            Returns:
                returns an integer representing the number of node in the list. Starts at 1, 0 means empty
        """
        counter = 0
        node = self.__head
        while node:
            counter += 1
            node = node.next_node
        return counter

    def printer(self):
        """Prints all elements of the list. For debugging purposes only"""
        node = self.__head
        while node is not None:
            if node is self.__head:
                print("i am the head : " + node.item + " My next node is " + node.nextNode.item)
            elif node.nextNode is None:
                print("i am the tail : " + node.item)
            else:
                print("i am " + node.item + " My next node is " + node.nextNode.item)
            node = node.nextNode

    def insert_at(self, item, index):
        """ Insert an item at the specified index, preserving the previous index
            Args:
                item (object): The item to be inserted in the list.
                index (int): The location in the list where to insert the item
         """
        if not 0 <= index <= len(self):
            raise IndexError('Provided index is out of bounds')

        previous_node = None
        current_node = self.__head

        if index == 0:
            self.__head = Node(item, self.__head)
            if self.__tail is None:
                self.__tail = self.__head
            return

        counter = 0

        while counter < index:
            counter += 1
            previous_node = current_node
            current_node = current_node.next_node

        previous_node.next_node= Node(item, current_node)

    def add_back(self, item):
        """ Add an item to the head of the list
            Args:
                item (object): The item to be inserted in the list.
        """
        if self.__head is None:
            self.__head = Node(item)
            self.__tail = self.__head
            return
        self.__tail.next_node = Node(item)
        self.__tail = self.__tail.next_node
        return

    def add_front(self, item):
        """ Add an item to the tail of the list
            Args:
                item (object): The item to be inserted in the list.
        """
        self.insert_at(item, 0)

    def remove(self, index):
        """ remove an item with the corresponding index
            Args:
                index (int): The location of the item to be removed
            Returns:
                returns the removed item
        """
        if not 0 <= index < self.length():
            return IndexError('Provided index is out of bounds')
        previous_node = None
        current_node = self.__head

        if index == 0:
            self.__head = self.__head.next_node
            return
        
        counter = 0
        
        while counter < index:
            counter += 1
            previous_node = current_node
            current_node = current_node.next_node
        to_return = current_node
        previous_node.next_node = None
        return to_return.item

    def remove_back(self):
        """ remove the head of the list
            Returns:
                return the removed head
        """
        return self.remove(len(self)-1)

    def remove_front(self):
        """remove the tail of the list
            Returns:
                return the removed tail
        """
        return self.remove(0)

    def get(self, index):
        """ return the item specified at the index
            Args:
                index (int): The location of the item to return
            Returns:
                return the value item of the node matching the index provided
        """
        if not 0 <= index < self.length():
            return IndexError('Provided index is out of bounds')
        counter = 0
        current_node = self.__head
        while counter < index:
            counter += 1
            current_node = current_node.next_node
        return current_node.item

    def put(self, item, index):
        """ change the value of the item at the index provided
            Args:
                item (object): The item to be added in the list.
                index (int): The location of the item to be changed
        """
        if not 0 <= index < self.length():
            return IndexError('Provided index is out of bounds')
        counter = 0
        current_node = self.__head
        while counter is not index:
            counter += 1
            current_node = current_node.next_node
        current_node.item = item

    def find(self, item):
        """ Tries to find the index for the corresponding item
            Args:
                item (object): The item to be inserted in the list.
            Returns:
                returns the index of the item in the list. If the item does not exist return -1
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
        """ concatenate two linkedList that are not None
            Args:
                other (LinkedList): the other list to be added to self
        """
        for i in other:
            self.add_back(i)
        return

    def length(self):
        """
            Returns:
                return the length via __len__ of the list
        """
        return len(self)

    def is_empty(self):
        """
            Returns:
                return True if the list is empty or False if the list is not empty
        """
        if len(self) == 0:
            return True
        else:
            return False

    def __iter__(self):
        current_node = self.__head
        while current_node is not None:
            yield current_node.item
            current_node = current_node.next_node

