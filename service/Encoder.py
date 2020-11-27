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
        original_data = file_helper.get_contents()
        huff_data = huff.get_huff_list()
        #:  On créée une représentation binaire sous forme de string de notre fichier compressé.
        binary = ""
        for symbol in original_data:
            for i in huff_data:
                if i.symbol == symbol:
                    binary += i.binary
                    break
        #:  On sérialise le header pour pouvoir décoder notre fichier plus tard.
        header = self.header_serialiser(huff_data)
        header = bytearray(header, encoding="utf8")
        #:  On transforme notre représentation binaire en char utf8.
        byte_array = self.binary_helper.make_byte_array(binary)
        #:  On écrit le tout dans notre fichier compressé.
        file_helper.write_binary(header + byte_array,self.extension)

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