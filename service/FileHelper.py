from adt.dictionnary.BSTDictionnary import BSTDict
from adt.list.ArrayList import ArrayList
from adt.list.SortedList import DescSortedList
from model.HuffData import HuffData
from model.HuffTable import HuffTable
from model.HuffTree import HuffNode
from service.BinaryHelper import BinaryHelper


class FileHelper:
    """
    Classe permettant de lire et d'écrire des fichiers.
    """

    def __init__(self, filename: str, folder: str):
        self.filename = filename
        self.folder = folder
        self.buffer = ArrayList()
        self.binary_helper = BinaryHelper()
        self.compressed_extension = '.pluspetit'
        self.decompressed_extension = '.txt'

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
        for entry in symbol_count.inorder():  #:    On ordonne notre char count de façon descendante pour la construction du hufftree.
            to_return.push(HuffNode(entry.key, entry.value))
        return to_return

    def get_contents(self):
        #:  Lit un fichier et renvoie le contenu au fur et à mesure sous forme d'un string.
        path = self.folder + self.filename + self.decompressed_extension
        file = open(path, encoding="utf8")
        for symbol in file.read():
            yield symbol
        file.close()

    def write_bytes(self, content):
        #:  Écrit en utf8 dans un fichier à partir d'un bytearray.
        path = self.folder + self.filename + self.compressed_extension
        file = open(path, "wb")
        file.write(content)
        file.close()

    def write_bit(self, content):
        #:  Écrit en utf8 dans un fichier à partir d'un bytearray.
        self.buffer.add_back(content)
        if len(self.buffer) == 8:
            path = self.folder + self.filename + self.compressed_extension
            file = open(path, "ab")
            file.write(bytes([self.binary_helper.to_int(self.buffer)]))
            self.buffer.clear()
            file.close()

    def write_text(self, content, extension):
        #:  Écrit du texte dans un fichier.
        path = self.folder + self.filename + extension
        file = open(path, "w")
        file.write(content)
        file.close()

    def unpack_file(self):
        #:  Permet de recréer un hufftable a partir d'un fichier compressé et d'en séparer les données.
        compressed_file = open(self.folder + self.filename + self.compressed_extension, "rb")
        #:  On vide le fichier décompressé si il existe, ensuite on l'ouvre pour pouvoir ajouter à mesure qu'on lit
        open(self.folder + self.filename + self.decompressed_extension, "w").close()
        decompressed_file = open(self.folder + self.filename + self.decompressed_extension, "a")
        current = ''
        key_len = 0
        header_size = 0
        header_start= False

        symbol, frequency, binary = ["",0 ,""]
        position = 0  # 0 = symbol, 1 = binary, 2 = frequency

        hufftable = HuffTable()
        for char in compressed_file.read():
            #: La première section permet d'aller chercher la table de huffman
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
            #: La deuxième section permet de réécrire un fichier txt
            else:
                current += self.binary_helper.to_bits(char)
                while key_len < len(current):
                    key_len += 1
                    try:
                        huffdata = hufftable[current[:key_len]]
                        if huffdata.frequency > 0:
                            decompressed_file.write(huffdata.symbol)
                            huffdata.frequency -= 1
                            current = current[key_len:]
                            key_len = 0
                        else:
                            break
                    except KeyError:
                        pass
        compressed_file.close()
        decompressed_file.close()
