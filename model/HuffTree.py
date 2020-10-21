from adt.dictionnary.HashTable import HashTable
from adt.list import SortedList
from adt.list.LinkedList import LinkedList
from adt.list.IList import IList
from adt.queue.Queue import Queue
from unused.MinHeap import MinHeap
from model.HuffData import HuffData


class HuffNode:
    """
    Représente un noeud de notre arbre de huffman.

    Attributes:
        key (int): représente la fréquence d'un caractère ou simplement, la fréquence d'un ensemble de caractères, si la "value" est None.
        value (str): Représente le caractère ou rien.
        left_child (HuffNode): Représente l'enfant de gauche qui devra être stocké lorsque nous créerons l'arbre de Huffman
        right_child (HuffNode): Représente l'enfant de droite qui devra être stocké lorsque nous créerons l'arbre de Huffman
    """
    def __init__(self, char, frequency, left_child=None, right_child=None):
        self.key = frequency
        self.value = char
        self.left_child = left_child
        self.right_child = right_child

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __str__(self):
        return f"('{self.value}', {self.key})"


class HuffTree:
    """
    Implementation de l'arbre de huffman qui transformeras une Liste de HuffData en un hufftree.
    """
    def __init__(self, data: SortedList):
        self.root = self.__huffify(data)

    def __build_min_heap(self, data: IList):
        """
        Permet de peupler le MinHeap des HuffData que nous avons trié plus tôt.

        Args:
            data (IList): Représente la liste de données que nous voulons transformer en MinHeap HuffData que nous utiliserons.
        """
        minheap = MinHeap()
        while data:  #: Aussi longtemps que nous avons des HuffData dans la liste.
            to_insert = data.remove_back()  #: Nous retirons le dernier élément(celui avec la plus grande fréquence)
            new_node = HuffNode(to_insert.symbol, to_insert.frequency)  #: Nous le transformons en un noeud de l'arbre
            minheap.insert(new_node)  #: Nous ajoutons ce nouveau noeud à l'arbre.
        return minheap

    def __huffify(self, data: SortedList):
        """
        Transformer une liste de donnée en hufftree

        Args:
            data (IList): Représente les données que nous voulons transformer en HuffTree

        Returns:
            La racine du HuffTree.
        """
        while len(data) > 1:     #: On construit un huff tree donc aussi longtemps qu'il y a plus d'un noeud, on combine les 2 plus petits noeuds dans un noeud qui n'a pas de valeur et qui a la sommme de leur fréquence comme clé.
            first_node = data.remove_back()
            second_node = data.remove_back()
            combined_frequency = first_node.key + second_node.key
            new_node = HuffNode(None, combined_frequency, first_node, second_node)
            data.push(new_node)
        return data[0]

    def get_huff_table(self):
        """
        Permet de générer un huff table avec notre hufftree

        Returns:
            Un HashTable qui a été construit avec notre HuffTree et qui a pour clée le code binaire de notre HuffData.
        """
        huff_table = HashTable()
        for data in iter(self):
            if data.symbol:
                huff_table[data.binary] = data
        return huff_table

    def get_huff_list(self):
        """
        Permet de générer une liste avec le huffdata contenu dans notre hufftree

        Returns:
            Une liste de tout le huff data contenu dans le hufftree.
        """
        huff_list = LinkedList()
        for data in iter(self):
            if data.symbol:
                huff_list.add_back(data)
        return huff_list

    def __iter__(self):
        """
        Permet de parcourir et de renvoyer chaque noeud de l'arbre sous forme HuffData dans un ordre Breadth First.
        Yields:
             Every HuffNode of the HuffTree containing a char in a breadth first order as HuffData.
        """
        huff_node_queue = Queue()   #: Queue qui nous servira à parcourir tout l'arbre
        huff_data_queue = Queue()   #: Queue qui nous servira à créer les huffdata hors des noeuds de notre arbre.
        huff_node_queue.push(self.root)   #: On met le premier élément dans le queue
        huff_data_queue.push(HuffData(self.root.value, self.root.key, ""))
        while not huff_node_queue.is_empty(): #: Aussi longtemps qu'il y a des éléments dans le queue des noeuds, on retire le premier et on ajouter les enfants de celui-ci dans chaque queue. Si l'enfant est None, rien est ajouté.
            first_node = huff_node_queue.pop()
            first_data = huff_data_queue.pop()
            if first_node.left_child: #: Si enfant gauche, on l'ajoute dans le node queue et on ajoute un node data qui a les mêmes informations et sa valeur binaire, sois celle du parent avec un 0 de plus.
                huff_node_queue.push(first_node.left_child)
                binary = f"{first_data.binary}0"
                huff_data_queue.push(HuffData(first_node.left_child.value, first_node.left_child.key, binary))
            if first_node.right_child:  #: Si enfant droite, on l'ajoute dans le node queue et on ajoute un node data qui a les mêmes informations et sa valeur binaire, sois celle du parent avec un 1 de plus.
                huff_node_queue.push(first_node.right_child)
                binary = f"{first_data.binary}1"
                huff_data_queue.push(HuffData(first_node.right_child.value, first_node.right_child.key, binary))
            yield first_data
        return


