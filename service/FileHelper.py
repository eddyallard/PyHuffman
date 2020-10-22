from adt.dictionnary.BSTDictionnary import BSTDict
from adt.dictionnary.HashTable import HashTable
from adt.list.SortedList import DescSortedList
from model.HuffData import HuffData
from model.HuffTree import HuffNode


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
        symbol_count = BSTDict()  #: Le comptage initial des symbols se fait dans un BSTDict, car il nous permet de chercher et de modifier des entrées en un temps O(log N) à O(n) dépendament du balancement de l'arbre.
        to_return = DescSortedList()  #: Les symboles et leur nombre d'occurence est ensuite mis dans une liste ordonnée ce qui facilitera les opérations futures.
        path = self.folder + self.filename + ".txt"
        file = open(path, encoding="utf8")  #: Maintenant nous lisons le fichier au path fournit.
        for symbol in file.read():  #: On évalue chaque symbole.
            try:  #: On incrémente la valeur(nb d'occurences) du symbole de 1.
                symbol_count[symbol] += 1
            except (AttributeError, KeyError):  #: S'il n'existe pas, ces erreur sont levées alors on l'initialise.
                symbol_count[symbol] = 1
        file.close()

        while symbol_count.root:  #: On vide le BSTDict dans la liste ordonnée pour faciliter les opérations futures.
            popped = symbol_count.pop_leftmost()
            to_return.push(HuffNode(popped.key, popped.value))

        return to_return

    def get_contents(self):
        to_return = ""
        path = self.folder + self.filename + ".txt"
        file = open(path, encoding="utf8")
        for symbol in file.read():
            to_return += symbol
        file.close()
        return to_return

    def write_binary(self, content, extension):
        path = self.folder + self.filename +extension
        file = open(path, "wb")
        file.write(content)
        file.close()

    def write_text(self, content, extension):
        path = self.folder + self.filename + extension
        file = open(path, "w")
        file.write(content)
        file.close()

    def unpack_file(self,extension):
        compressed_file = open(self.folder + self.filename + extension, "rb")

        current = ""
        header_size = 0
        header_start= False

        symbol, frequency, binary = ["",0 ,""]
        position = 0  # 0 = symbol, 1 = binary, 2 = frequency

        hufftable = HashTable()
        data = bytearray()
        for char in compressed_file.read():
            if not header_start:
                if chr(char) == "/":
                    header_size = int(current)
                    header_start = True
                    current = ""
                else:
                    current += chr(char)
            elif header_size > 0:
                if chr(char) == "/":
                    if position == 0:
                        symbol = current
                        position += 1
                    elif position == 1:
                        binary = current
                        position += 1
                    else:
                        frequency = int(current)
                        hufftable[binary] = HuffData(symbol, frequency, binary)
                        symbol, frequency, binary = ["", 0, ""]
                        position = 0
                    current = ""
                else:
                    current += chr(char)
                header_size -= 1
            else:
                data.append(char)
        compressed_file.close()
        return hufftable, data
