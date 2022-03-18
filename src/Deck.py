from Card import Card  	         	  
from RandNumberSet import RandNumberSet


class Deck():  	         	  
    def __init__(self, card_size, num_cards, max_num):  	         	  
        """  	         	  
        Deck constructor  	         	  
        """
        self.card_size = int(card_size)
        self.num_cards = int(num_cards)
        self.max_num = int(max_num)
        self.idnum = 1
        self.RNS = RandNumberSet(self.card_size, self.max_num)
        rowsShuffled = 0
        self.RNS.shuffle()
        while rowsShuffled < len(self.RNS):
            self.c = self.RNS.next_row()
            if self.c != None:
                Card(self.idnum, self.c)
                rowsShuffled += 1
                self.idnum += 1
            else:
                continue



    def __len__(self):  	         	  
        """  	         	  
        Return an integer: the number of cards in this deck  	         	  
        """
        return int(self.num_cards)


    def card(self, n):  	         	  
        """  	         	  
        Retrieve Card N from the deck  	         	  
        """
        self.n = int(n)
        #return Card(self.n, self.RNS)


    def __str__(self):  	         	  
        """  	         	  
        Return None: Display the entire Deck as a string  	         	  
        """
        output = ""
        while self.idnum <= int(self.num_cards):
            c = str(Card(self.idnum, self.c))
            output += c
        return output
        pass  	         	  
