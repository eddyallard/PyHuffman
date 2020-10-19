class HuffData(object):
    def __init__(self, symbol, frequency, binary=None):
        self.symbol = symbol
        self.frequency = frequency
        self.binary = binary

    def __lt__(self, other):
        if self.frequency < other.frequency:
            return True
        elif self.frequency == other.frequency:
            if self.symbol > other.symbol:
                return True
        else:
            return False

    def __gt__(self, other):
        if self.frequency > other.frequency:
            return True
        elif self.frequency == other.frequency:
            if self.symbol < other.symbol:
                return True
        else:
            return False

    def __str__(self):
        return f"('{self.symbol}',{self.frequency},{self.binary})"

