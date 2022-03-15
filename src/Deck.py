from Card import Card  	         	  
from RandNumberSet import RandNumberSet  	         	  


class Deck():  	         	  
    def __init__(self, card_size, num_cards, max_num):  	         	  
        """  	         	  
        Deck constructor  	         	  
        """
        self.card_size = card_size
        self.num_cards = num_cards
        self.max_num = max_num
        pass  	         	  

    def __len__(self):  	         	  
        """  	         	  
        Return an integer: the number of cards in this deck  	         	  
        """
        return self.num_cards
        pass  	         	  

    def card(self, n):  	         	  
        """  	         	  
        Retrieve Card N from the deck  	         	  
        """  	         	  
        pass  	         	  

    def __str__(self):  	         	  
        """  	         	  
        Return None: Display the entire Deck as a string  	         	  
        """  	         	  
        pass  	         	  
