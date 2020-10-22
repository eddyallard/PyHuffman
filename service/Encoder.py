from adt.dictionnary.HashTable import HashTable
from model.HuffTree import HuffTree
from model.HuffData import HuffData
from service.BinaryHelper import BinaryHelper
from service.FileHelper import FileHelper


class Encoder:
    def __init__(self, filename, path, extension=".alexandro"):
        self.path = path
        self.filename = filename
        self.binary_helper = BinaryHelper()
        self.extension = extension

    def encode(self):
        file_helper = FileHelper(self.filename, self.path)
        huff = HuffTree(file_helper.fetch_symbols())
        original_data = file_helper.get_contents()
        # compressed_file = open(self.path + self.filename + self.extension, "wb")
        huff_data = huff.get_huff_list()
        binary = ""

        for symbol in original_data:
            for i in huff_data:
                if i.symbol == symbol:
                    binary += i.binary
                    break

        header = self.header_serialiser(huff_data)
        header = bytearray(header, encoding="utf8")
        # compressed_file.write(header)
        byte_array = self.binary_helper.make_byte_array(binary)
        file_helper.write_binary(header + byte_array,self.extension)
        # compressed_file.write(byte_array)
        # compressed_file.close()
        # self.unpack_file() why is this here ???

    def header_serialiser(self, huff_data):
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

    def unpack_file(self):
        # to put in filehelper maybe??
        compressed_file = open(self.path + self.filename + self.extension, "rb")

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

    def decode(self):
        file_helper = FileHelper(self.filename,self.path)
        hufftable, data = self.unpack_file()
        binary_helper = BinaryHelper()
        binary_data = binary_helper.make_bits_string(data)
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
        file_helper.write_text(file_content, self.path,self.filename, ".txt")
        return file_content