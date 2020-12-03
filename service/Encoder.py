from model.HuffTree import HuffTree
from service.BinaryHelper import BinaryHelper
from service.FileHelper import FileHelper


class Encoder:
    """
    Classe qui permet à encoder et décoder les fichiers.
    """
    def __init__(self, filename, path, extension=".pluspetit"):
        self.path = path
        self.filename = filename
        self.binary_helper = BinaryHelper()
        self.extension = extension

    def encode(self):
        #:  Utilisation de filehelper pour lire/écrire dans les fichiers.
        file_helper = FileHelper(self.filename, self.path)
        #:  On passe notre algo de huffman sur le tree.
        huff = HuffTree(file_helper.fetch_symbols())
        huff_data = huff.get_huff_list()
        #:  On sérialise le header et on l'écrit dans notre fichier.
        header = self.header_serialiser(huff_data)
        header = bytearray(header, encoding="utf8")
        file_helper.write_bytes(header)
        #:  On écrit bit par bit dans notre fichier comnpressé
        for symbol in file_helper.get_contents():
            for i in huff_data:
                if i.symbol == symbol:
                    for bit in i.binary:
                        file_helper.write_bit(bit)
                    break
        #: On écrit les derniers bits en ajoutant des 0 pour avoir un byte.
        while len(file_helper.buffer) != 0:
            file_helper.write_bit('0')

    def header_serialiser(self, huff_data):
        #: Permet de sérialiser notre huff data sous la forme /a/011/567/.
        serialized = ""
        for data in huff_data:
            serialized += "/"
            serialized += data.symbol
            serialized += "/"
            serialized += data.binary
            serialized += "/"
            serialized += str(data.frequency)
        serialized = str(len(serialized)) + serialized + "/"
        return serialized

    def decode(self):
        #:  Utilisation de filehelper pour lire/écrire dans les fichiers.
        file_helper = FileHelper(self.filename,self.path)
        #:  Division de notre hufftable et de notre string de data.
        hufftable, data = file_helper.unpack_file(self.extension)
        #:  Binary helper pour transforme notre string de data en une représentation binaire.
        binary_helper = BinaryHelper()
        binary_data = binary_helper.make_bits_string(data)
        #:  On traverse la représentation binaire pour recréer le texte original.
        file_content = ""
        current_binary = ""
        for bit in binary_data:
            current_binary += bit
            try:
                huffdata = hufftable[current_binary]
                if huffdata.frequency > 0:
                    file_content += huffdata.symbol
                    huffdata.frequency -= 1
                    current_binary = ""
                else:
                    break
            except KeyError:
                pass
        file_helper.write_text(file_content, ".txt")
        return file_content