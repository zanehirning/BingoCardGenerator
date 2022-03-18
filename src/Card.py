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
        print('     '.join(self.colNames))

        #if checkOdd != 0:
        #    midRow = (len(self.__ns) // (len(self.__ns) / 2)) - 1
        #    midCol = (len(self.__ns) // (len(self.__ns) / 2)) - 1
        #    self.__ns[int(midRow)][int(midCol)] = "Free!"
        #else:
        #    print(self.__ns)



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
        pass

    def __str__(self):
        """  	         	  
        Return a string: a neatly formatted, square bingo card  	         	  
        """
        card = ''
        card += print('     '.join(self.colNames))
        return "fadslfjksa"
        pass
