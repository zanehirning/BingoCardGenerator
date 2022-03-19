from Card import Card  	         	  
from RandNumberSet import RandNumberSet


class Deck():  	         	  
    def __init__(self, card_size, num_cards, max_num):  	         	  

        self.card_size = int(card_size)
        self.num_cards = int(num_cards)
        self.max_num = int(max_num)
        self.__deck = []
        for i in range(self.num_cards):
            RNS = RandNumberSet(self.card_size, self.max_num)
            c = Card(i + 1, RNS)
            self.__deck.append(c)

    def __len__(self):
        return int(self.num_cards)


    def card(self, n):
        return self.__deck[int(n)-1]


    def __str__(self):
        output = ""
        for i in range(self.num_cards):
            c = str(self.__deck[i])
            output += c
        print(output)
        return output
