from adt.list.ArrayList import ArrayList
from adt.tree.HuffTree import HuffTree
from model.HuffData import HuffData
from model.HuffTable import HuffTable
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
        original_file = open(self.path + self.filename+".txt", "r")
        compressed_file = open(self.path + self.filename + self.extension, "ab")
        compressed_file_header = open(self.path + self.filename + self.extension, "w")
        huff_data = huff.get_huff_list()
        binary = ""
        for symbol in original_file.read():
            try:
                for i in huff_data:
                    if i.symbol == symbol:
                        binary += i.binary
                        break
            except (AttributeError, KeyError):
                pass
        header = self.header_helper(huff_data)
        compressed_file_header.write(header)
        compressed_file_header.close()
        byte_array = self.binary_helper.make_byte_array(binary)
        compressed_file.write(byte_array)
        compressed_file.close()
        original_file.close()

    def header_helper(self, huff_data):
        table = ""
        counter = 0
        for i in huff_data:
            if i is not None:
                table += i.symbol
                table += i.binary
                counter += i.frequency
        table += table[0]
        table = str(counter) + table
        return table

    def decode(self):
        frequency, table,offset = self.fetch_header_from_file()



    def fetch_header_from_file(self):
        compressed_file = open(self.path + self.filename + self.extension, "r", errors='ignore')
        start_flag = True
        end_char = ""
        table = ArrayList()
        total_frequency = ""
        huffchar = ""
        huffbin = ""
        offset = 0
        for symbol in compressed_file.read():
            offset += 1
            print("benis")
            if symbol.isdigit() and start_flag:
                total_frequency += symbol
            elif symbol.isascii() and symbol.isdigit() is not True and start_flag:
                end_char += symbol
                huffchar = symbol
                end_char = symbol
                start_flag = False
            elif symbol.isdigit():
                huffbin += symbol
            elif symbol.isascii() and symbol.isdigit() is not True and symbol is not end_char:
                table.add_back(HuffData(huffchar, None, huffbin))
                huffchar = symbol
                huffbin = ""
            elif symbol is end_char:
                break
        print(total_frequency)

        return total_frequency, table, offset