from adt.dictionnary.BSTDictionnary import BSTDict
from adt.list.SortedList import DescSortedList
from model.HuffData import HuffData
from adt.tree.HuffTree import HuffTree


class FileHelper:
    """
    Classe permettant de lire et d'écrire des fichiers.
    """
    def __init__(self, filename: str, folder: str):
        self.filename = filename
        self.folder = folder

    def fetch_symbols(self):
        """
        Permet de lire un fichier txt et de retourner une liste ordonnée des symboles et de leur nombre d'occurences.
        Returns:
            SortedList comportant le HuffData associé au fichié qui a été lu.
        """
        symbol_count = BSTDict()    #: Le comptage initial des symbols se fait dans un BSTDict, car il nous permet de chercher et de modifier des entrées en un temps O(log N) à O(n) dépendament du balancement de l'arbre.
        to_return = DescSortedList()    #: Les symboles et leur nombre d'occurence est ensuite mis dans une liste ordonnée ce qui facilitera les opérations futures.
        path = self.folder + self.filename
        file = open(path)     #: Maintenant nous lisons le fichier au path fournit.
        for symbol in file.read():  #: On évalue chaque symbole.
            try:    #: On incrémente la valeur(nb d'occurences) du symbole de 1.
                symbol_count[symbol] += 1
            except (AttributeError, KeyError):  #: S'il n'existe pas, ces erreur sont levées alors on l'initialise.
                symbol_count[symbol] = 1
        file.close()

        while symbol_count.root:    #: On vide le BSTDict dans la liste ordonnée pour faciliter les opérations futures.
            popped = symbol_count.pop_leftmost()
            to_return.push(HuffData(popped.key, popped.value))

        return to_return
