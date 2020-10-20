from adt.list.ArrayList import ArrayList
from adt.tree.HuffTree import HuffTree
from model.HuffTable import HuffTable
from service.BinaryHelper import BinaryHelper
from service.FileHelper import FileHelper


class Encoder:
    def __init__(self, filename, path):
        self.path = path
        self.filename = filename
        self.binary_helper = BinaryHelper()

    def encode(self):
        file_helper = FileHelper(self.filename, self.path)
        huff = HuffTree(file_helper.fetch_symbols())
        original_file = open(self.path + self.filename, "r")
        compressed_file = open(self.path + "binboi.bin", "wb")
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
        header_helper(huff_data)
        byte_array = self.binary_helper.make_byte_array(binary)
        compressed_file.write(byte_array)
        compressed_file.close()
        original_file.close()

    def decode(self):
        pass

    def header_helper(self,huff_data):
        table = ""
        start_symbol = None
        for i in huff_data:
            if i is not None:
                table += i.symbol
                start_symbol = i.symbol




