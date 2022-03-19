class Card():
    COLUMN_NAMES = list("BINGODARLYZEMPUX")

    def __init__(self, idnum, ns):
        self.__idnum = idnum
        self.__ns = ns

    def id(self):
        return self.__idnum

    def number_at(self, row, col):
        checkOdd = len(self.__ns) % 2
        if checkOdd != 0:
            midRow = (len(self.__ns) // 2)
            if row == midRow and col == midRow:
                return "Free!"
        return self.__ns[row][col]

    def __len__(self):
        return len(self.__ns)

    def __str__(self):
        header = '   '
        self.colNames = Card.COLUMN_NAMES[0:len(self.__ns)]
        header += '     '.join(self.colNames)
        card = ''
        spaces = ''
        for i in range(len(self.__ns)):
            spaces += "+-----"
        spaces += "+\n"

        for r in range(len(self.__ns)):
            for c in range(len(self.__ns)):
                card += f"|{self.number_at(r, c) : ^5}"
            card += "|" + "\n" + spaces

        return header + "\n" + spaces + card + "\n"

