class HuffData:
    """"
        Args:
            symbol : Symbol unicode que représente ce HuffData
            frequency : Nombre d'apparitions de ce symbole dans le texte
            binary : Représentation binaire du symbole pour la compression sous forme de string.
    """
    def __init__(self, symbol, frequency, binary=None):
        self.symbol = symbol
        self.frequency = frequency
        self.binary = binary

    def __lt__(self, other):
        """
            Returns:
                True si la fréquence du symbole est plus petite ou si la fréquence du symbole est égale, mais que son
                symbole apparait après celui de l'autre dans la table unicode.
        """
        if self.frequency < other.frequency:
            return True
        elif self.frequency == other.frequency:
            if self.symbol > other.symbol:
                return True
        else:
            return False

    def __gt__(self, other):
        """
            Returns:
                True si la fréquence du symbole est plus grande ou si la fréquence du symbole est égale, mais que son
                symbole apparait avant celui de l'autre dans la table unicode.
        """
        if self.frequency > other.frequency:
            return True
        elif self.frequency == other.frequency:
            if self.symbol < other.symbol:
                return True
        else:
            return False

    def __str__(self):
        return f"('{self.symbol}',{self.frequency},{self.binary})"

