from adt.list.ArrayList import ArrayList
from adt.tree.HuffTree import HuffTree
from model.HuffTable import HuffTable
from service.FileHelper import FileHelper


class Encoder:
    def __init__(self, TxtName, Path):
        self.Path = Path
        self.TxtName = TxtName

    def encode(self):
        fileHelper = FileHelper(self.TxtName, self.Path)
        huff = HuffTree(fileHelper.fetch_symbols())
        file = open(self.Path + self.TxtName, "r")
        cmpfile = open(self.Path + "binboi.bin", "w")
        charlist = self.__get_all_chars(huff)
        for symbol in file.read():
            try:
                for i in charlist:
                    if i.symbol == symbol:
                        cmpfile.write(i.binary)
            except (AttributeError, KeyError):
                pass
        cmpfile.close()
        file.close()

    def decode(self):
        pass

    def __get_all_chars(self, huff):
        list = ArrayList()
        itr = iter(huff)
        for a in itr:
            list.add_front(a)
        return list
    def __convert_str_bin(self,array):
        return int(array,2)
