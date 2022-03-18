class Card():
    COLUMN_NAMES = list("BINGODARLYZEMPUX")

    def __init__(self, idnum, ns):
        """  	         	  
        Initialize a Bingo! card  	         	  
        """
        self.__idnum = idnum
        self.__ns = ns
        checkOdd = len(self.__ns) % 2
        self.colNames = Card.COLUMN_NAMES[0:len(self.__ns)]
        self.row = self.__ns[0:len(self.__ns)]

        header = '   '
        card = ''
        spaces = ''
        header += '     '.join(self.colNames) + '\n'
        colVal = 0
        rowComplete = False
        while rowComplete == False:
            spaces += "\n"
            card += "|"
            while colVal < len(self.__ns):
                header += "+-----"
                spaces += "+-----"
                card += '  ' + f'{self.__ns[colVal]}' + '  |'
                colVal += 1
            rowComplete = True
        spaces += "+"
        header += "+"
        card += spaces
        #print(header)
        print(card)

        #if checkOdd != 0:
        #    midRow = (len(self.__ns) // (len(self.__ns) / 2))
        #    midCol = (len(self.__ns) // (len(self.__ns) / 2))
        #    self.__ns[int(midRow)][int(midCol)] = "Free!"
        #    self.__idnum += 1
        #else:
        #    print(self.__ns)
        #    self.__idnum += 1



    def id(self):
        """  	         	  
        Return an integer: the ID number of the card  	         	  
        """
        return self.__idnum
        pass

    def number_at(self, row, col):
        """  	         	  
        Return an integer or a string: the value in the Bingo square at (row, col)  	         	  
        """
        self.row = row
        self.col = col
        return self.__ns[row][col]
        pass

    def __len__(self):
        """  	         	  
        Return an integer: the length of one dimension of the card.  	         	  
        For a 3x3 card return 3, for a 5x5 return 5, etc.  	         	  
        """
        return len(self.__ns)

    def __str__(self):
        """  	         	  
        Return a string: a neatly formatted, square bingo card  	         	  
        """
        completeCard = ''
        card = '   '
        spaces = ''
        card += '     '.join(self.colNames) + '\n'
        spaces += "\n+-----"
        spaces += "+\n"
        n = 0
        colVal = 0
        rowComplete = False
        while rowComplete == False:
            spaces += "\n+-----"
            card += spaces
            card += "|"
            while n < len(self.__ns):
                card += '  ' + f'{self.__ns[colVal]}' + '  |'
                colVal += 1
                n += 1
            rowComplete = True
        card += spaces
        print(card)
    pass
